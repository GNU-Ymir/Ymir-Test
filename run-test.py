import yaml
import argparse
import glob
import os, shutil
import ntpath
from typing import Any
import subprocess 
import logging, sys
import re

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#The background is set with 40 plus the number of the color, and the foreground with 30

#These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"

def formatter_message(message, use_color = True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message

COLORS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'SUCCESS': GREEN,
    'ERROR': RED
}

SUCCESS = 5

class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color = True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            levelname_color = COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)

# Custom logger class with multiple destinations
class ColoredLogger(logging.Logger):
    FORMAT = "[$BOLD%(name)-20s$RESET][%(levelname)-18s]  %(message)s ($BOLD%(filename)s$RESET:%(lineno)d)"
    COLOR_FORMAT = formatter_message(FORMAT, True)
    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.DEBUG)                

        color_formatter = ColoredFormatter(self.COLOR_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return

    def success(self, msg, *args, **kwargs):
        self._log(SUCCESS, msg, args, **kwargs)
        
    

def diff (a : str, b : str):
    for i in range (0, min (len (a), len (b))):
        if (a [i] != b [i]):
            return "At : " + str (i) + " (" + str (a [:i+1]) + ":[" + str (a [i]) + "]) (" + str (b [:i]) + ":" + str (b [i]) + ")"
    return "Diff len"
        
def checkStdout (yml: dict, text : str, cwd : str):    
    if (type (yml) is dict) :
        with open (cwd + "/" + yml["file"]) as stream:
            txt = stream.read ()
            return (txt == text, txt)
    else :
        return (yml == text, yml)

def parseTest (path : str):    
    with open (path) as stream :
        try :
            FORMAT = "[\033[31m{0!s}\033[0m]" 
            logging.Logger.info ("Running test : " + FORMAT.format (path))
            cwd = os.path.dirname (path)
            yamlContent = yaml.load (stream, Loader=yaml.FullLoader)
            output = ""
            err = ""
            code = 0
            compile_out = ""
            compile_err = ""
            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            failed = False
            if ("compile" in yamlContent) :
                if (type (yamlContent["compile"]) is list):
                    for i in yamlContent ["compile"]: 
                        compile = i.split ()
                        r = subprocess.run (compile, capture_output=True, cwd=cwd)                
                        compile_out = compile_out + ansi_escape.sub('', (r.stdout.decode("utf-8")))
                        compile_err = compile_err + ansi_escape.sub('', (r.stderr.decode ("utf-8")))
                else:
                    compile = yamlContent["compile"].split ()
                    r = subprocess.run (compile, capture_output=True, cwd=cwd)                
                    compile_out = compile_out + ansi_escape.sub('', (r.stdout.decode("utf-8")))
                    compile_err = compile_err + ansi_escape.sub('', (r.stderr.decode ("utf-8")))                   
            else :
                logging.Logger.error ("No 'compile' directive " + path)
                failed = True

            test_compile_out = ""
            if ("compile_out" in yamlContent):
                test_compile_out = yamlContent["compile_out"]
            
            (ok, txt) = checkStdout (test_compile_out, compile_out, cwd)
            if not ok:
                logging.Logger.error ("Test failed " + path);
                logging.Logger.error ("Expected compile out : [" + txt + "]")
                logging.Logger.error ("Got : [" + compile_out + "]")
                logging.Logger.error ("Diff : [" + diff (compile_out, txt) + "]")
                failed = True                    

            test_compile_err = ""
            if ("compile_err" in yamlContent):
                test_compile_err = yamlContent["compile_err"]
                
            
            (ok, txt) = checkStdout (test_compile_err, compile_err, cwd)
            if not ok:
                logging.Logger.error ("Test failed " + path);
                logging.Logger.error ("Expected compile err : [" + txt + "]")
                logging.Logger.error ("Got : [" + compile_err + "]")
                logging.Logger.error ("Diff : [" + diff (compile_err, txt) + "]")
                failed = True                
                
            if ("run" in yamlContent):
                try : 
                    if type (yamlContent["run"]) is list : 
                        for i in yamlContent ["run"]:
                            run = i.split ()
                            r = subprocess.run (run, cwd=cwd, capture_output=True)
                            output = output + ansi_escape.sub('', (r.stdout.decode("utf-8")))
                            err = err + ansi_escape.sub('', (r.stderr.decode ("utf-8")))
                    else :
                        run = yamlContent ["run"]
                        r = subprocess.run (run, cwd=cwd, capture_output=True)
                        output = output + ansi_escape.sub('', (r.stdout.decode("utf-8")))
                        err = err + ansi_escape.sub('', (r.stderr.decode ("utf-8")))
                except :
                    failed = True
                    
                test_stdout = ""
                if ("stdout" in yamlContent):
                    test_stdout = yamlContent["stdout"]
                
                (ok, txt) = checkStdout (test_stdout, output, cwd)
                if not ok:
                    logging.Logger.error ("Test failed " + path);
                    logging.Logger.error ("Expected stdout : [" + txt + "]")
                    logging.Logger.error ("Got : [" + output + "]")
                    logging.Logger.error ("Diff : [" + diff (output, txt) + "]")

                    failed = True

                test_stderr = ""    
                if ("stderr" in yamlContent):
                    test_stderr = yamlContent["stderr"]
                    
                (ok, txt) = checkStdout (test_stderr, err, cwd)
                if not ok:
                    logging.Logger.error ("Test failed " + path);
                    logging.Logger.error ("Expected stderr : [" + txt + "]")
                    logging.Logger.error ("Got : [" + err + "]")
                    logging.Logger.error ("Diff : [" + diff (err, txt) + "]")
                    failed = True

            if ("clean" in yamlContent):
                run = yamlContent ["clean"].split ()
                r = subprocess.run (run, cwd=cwd)

            if not failed:
                logging.Logger.success ("Test succeed " + path);
                
        except yaml.YAMLError as exc :
            logging.Logger.error ("Test failed " + i);
    

    
def parsePlaybook (path : str):
    cwd = os.path.dirname (path)
    if cwd == "" :
        cwd = "." 
    with open (path) as stream :
        try :
            yamlContent = yaml.load (stream, Loader=yaml.FullLoader)
            if "tests" in yamlContent : 
                for i in yamlContent["tests"] :
                    try: 
                        parseTest (cwd + "/" + i)
                    except :
                        logging.Logger.error ("Test failed " + str (cwd + "/" + i));
            if "sub-playbooks" in yamlContent :
                FORMAT = "[\033[34m{0!s}\033[0m]" 
                for i in yamlContent ["sub-playbooks"] :                    
                    logging.Logger.info ("Running sub playbook : " + FORMAT.format (str (i)))
                    parsePlaybook (cwd + "/" + i)
        except yaml.YAMLError as exc :
            print (exc)
            raise IllegalStateError (obj[key] + " : Yaml no valid")

def setupLogging (args: Any) :
    global DEBUG_LEVELS
    logging.addLevelName(5, 'SUCCESS')

    # If you want to debug jinja rendering
    #   DEBUG_LEVELS = DEBUG_LEVELS + [DEBUG_JINJA_LEVEL]

    # If you want to debug states rendering (and dump the dot files in /tmp/{role name}.dot)      
    logging.basicConfig(level=logging.DEBUG)
    
    logging.Logger = ColoredLogger ("test")

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)


        
def main (args: Any):
    if (args.test != None):
        try : 
            parseTest (args.test)
        except:
            logging.Logger.error ("Test failed " + args.test);
    else :
        parsePlaybook (args.playbook)

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()

    parser.add_argument("--playbook", help="playbook of tests")
    parser.add_argument("--test", help="playbook of tests", default=None)
    
    args = parser.parse_args()
    
    setupLogging (args)
    main (args)

import yaml
import argparse
import glob
import os, shutil
import ntpath
from typing import Any
import subprocess 
import logging, sys


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
        
    

def checkStdout (yml: dict, text : str, cwd : str):
    if (type (yml) is dict) :
        with open (cwd + "/" + yml["file"]) as stream:
            return stream.read () == text
    else :
        return yml == text

def parseTest (path : str):
    with open (path) as stream :
        try :
            logging.Logger.info ("Running test : " + path)
            cwd = os.path.dirname (path)
            yamlContent = yaml.load (stream, Loader=yaml.FullLoader)
            output = ""
            err = ""
            code = 0
            compile_out = ""
            compile_err = ""
            failed = False
            if ("compile" in yamlContent) :
                for i in yamlContent ["compile"]: 
                    compile = i.split ()
                    r = subprocess.run (compile, capture_output=True, cwd=cwd)                
                    compile_out = compile_out + (r.stdout.decode("utf-8"))
                    compile_err = compile_err + (r.stderr.decode ("utf-8"))
                
            if ("compile_out" in yamlContent):
                if not checkStdout (yamlContent["compile_out"], compile_out):
                    logging.Logger.error ("Test failed " + path);
                    failed = True                    
                
            if ("compile_err" in yamlContent):
                if not checkStdout (yamlContent["compile_err"], compile_err):
                    logging.Logger.error ("Test failed " + path);
                    failed = True
                
            if ("run" in yamlContent):
                for i in yamlContent ["run"]: 
                    run = i.split ()
                    r = subprocess.run (run, cwd=cwd, capture_output=True)
                    output = output + (r.stdout.decode("utf-8"))
                    err = output + (r.stderr.decode ("utf-8"))
                
            if ("stdout" in yamlContent):
                if not checkStdout (yamlContent["stdout"], output, cwd):
                    logging.Logger.error ("Test failed " + path);
                    logging.Logger.error ("Expected out : " + yamlContent["stdout"])
                    logging.Logger.error ("Got : " + output)
                    failed = True
                
            if ("stderr" in yamlContent):
                if not checkStdout (yamlContent["stderr"], err, cwd):
                    logging.Logger.error ("Test failed " + path);
                    failed = True

            if ("clean" in yamlContent):
                run = yamlContent ["clean"].split ()
                r = subprocess.run (run, cwd=cwd)

            if not failed:
                logging.Logger.success ("Test succeed " + path);
                
        except yaml.YAMLError as exc :
            print (exc)
            raise IllegalStateError (obj[key] + " : Yaml no valid")


    
def parsePlaybook (path : str):
    with open (path) as stream :
        try :
            yamlContent = yaml.load (stream, Loader=yaml.FullLoader)
            for i in yamlContent["tests"] :
                parseTest (i)
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
    parsePlaybook (args.playbook)

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()

    parser.add_argument("playbook", help="playbook of tests")

    args = parser.parse_args()
    
    setupLogging (args)
    main (args)

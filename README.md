# Ymir-Test

In this repository the test of the ymir compiler are registered
They can be used to verify that the compiler does what is intended

A test is registered in a playbook whose yaml format is the following :
```yaml
tests:
  - path/to/test.yml
  - path/to/second/test.yml
```

The format of a test is the following :
```yaml
compile: # the list of command to execute to compile the test
  - gyc main.yr -c main.o
  - gyc foo.yr -c foo.o
  - gyc main.o foo.o -o test
compile_out: "" # the expected text (concatenation of all the command stdout in compile), can be unset
compile_err: "" # the expected text (concatenation of all the command stderr in compile), can be unset
run: # The list of command to run to test the compiled program
  - ./test file.txt
stdout: "" # the expected output (concatenation of all run command stdout in run), can be unset
stderr: "" # the expected error output (concatenation of all run command stderr in run), can be unset
clean: rm test *.o # command to run to remove generated files, can be unset
```

The test are runnable with the python file run-test.py
```bash
python3 run-test.py --test path/to/test.yml ; single test
python3 run-test.py --playbook playbook.yml ; list of tests
```


 

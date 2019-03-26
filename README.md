# CS142 Assignment 3

- Parser1.py contains the function Parser1
- TranslatorTelugu.py contains the function TranslatorTelugu
- ParseFunc.py contains the function ParseFunc.py
- FuncGenerator.py contains the function FuncGenerator
- tests1.py runs tests on the first two functions
- test2.py runs tests on the second two functions

## Running on your computer

To use the Google Translate Api

Run the following command in your terminal

    $ pip install googletrans

If there's an error with the installation, it is possible that it is necessary to start a virtualenv to install the dependency.
Run the following commands to do so

    $ python3 -m venv env
    $  source ./env/bin/activate 
    
And re run the installation command.

Run the following commands to run the tests and see how the functions work

    $ python3 tests1.py
    $ python3 tests2.py

You should be able to see the application on http://127.0.0.1:5000/

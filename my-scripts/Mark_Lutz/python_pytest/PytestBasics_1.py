import pytest

'''
All tests/files/methods we write in pytest, should either start with 'test' keyword or end with 'test' keyword, only then they will be executed.

E.g. if we are inside python_pytest:
python_pytest/
├── __init__.py
├── PytestBasics_1.py
└── test_demo.py

and we run command "py.test" then only tests in test_demo.py will be executed as PytestBasics_1.py doesn't start or end with 'test' keyword.
Note: "py.test" runs tests in all the python files(which start with 'test' keyword or end with 'test' keyword) in our current directory
'''

#########To execute only specific python test/class/file
"py.test test_demo.py"  --> this will only execute tests in file test_demo.py

"py.test -k login -v"  --> this will only execute all methods/tests in all available file(start and end with 'test') having name 'login' (start & end wih 'test') in them
-k -> keyword identifier(only methods with his keyword will be executed)
-v -> more verbose results i.e. more info on console


##########To execute specific test cases based on markers
We can defined marker in below manner:

@pytest.mark.login
def test_m5():
    assert 100 == 100

-m -> marker. Test cases with defined marker will only run.
"py.test -m login -v" --> this will execute all methods/tests in all available file(start and end with 'test') having marker as "login" i.e. @pytest.mark.login
"py.test test_demo2.py -m login -v" --> this will only execute methods/tests in python file test_demo2.py having marker as "login" i.e. @pytest.mark.login


##########Run test cases in parallel mode
To run test cases in parallel mode we first have to install "pytest-xdist" package
"pip install pytest-xdist"


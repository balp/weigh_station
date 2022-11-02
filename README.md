Weigh Station Test Kata
=======================

This is a web applications that have a fair number of test cases.
The exersice is to add tests to catch a few bugs in the code. There
are unit-tests that cover 100% of the code statements. You can run
and view the functionality. With a somewhat expected functionality.

    ---------- coverage: platform win32, python 3.10.7-final-0 -----------
    Name                                Stmts   Miss  Cover
    -------------------------------------------------------
    weigh_station\__init__.py             7      0   100%
    weigh_station\routes.py               4      0   100%
    weigh_station\views\__init__.py       0      0   100%
    weigh_station\views\default.py       17      0   100%
    weigh_station\views\notfound.py       5      0   100%
    -------------------------------------------------------
    TOTAL                                  33      0   100%


The applications are build on the python [pyramid framework](https://trypyramid.com/).

Description
-----------

The applications have a front page that shows the summary of lorries that have passed
a weigh station. It has an endpoint where the weigh station uploads it's data to be shown. 
After running the application as below, you can se the summary on the front page and use the
request in lorry_passing.http to update the data in the server. There is also a simple python
program passing_lorry.py that will using requests post some new data for testing.

Getting Started
---------------

- Change directory into your newly created project if not already there. Your
  current directory should be the same as this README.txt file and setup.py.

    cd weigh_station

- Create a Python virtual environment, if not already created.

    python3 -m venv env

- Upgrade packaging tools, if necessary.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini

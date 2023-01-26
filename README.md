# python-test: a demo python repository with GitHub actions for code quality

## Live status:

[![Python test workflow](https://github.com/rjalexa/python-actions/actions/workflows/python-test.yml/badge.svg)](https://github.com/rjalexa/python-actions/actions/workflows/python-test.yml) [![Codecov](https://codecov.io/gh/rjalexa/python-actions/branch/main/graph/badge.svg?token=1F2VGHFJ3S)](https://codecov.io/gh/rjalexa/python-test) ![Linting](https://github.com/rjalexa/python-actions/actions/workflows/python-lint.yml/badge.svg) ![Formatting](https://github.com/rjalexa/python-actions/actions/workflows/python-format.yml/badge.svg)

## Tooling

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-black.svg?style=flat)](https://github.com/rjalexa/myproject/issues) [![linting: pylint](https://img.shields.io/badge/linting-pylint-black)](https://github.com/PyCQA/pylint) ![Formatter](https://img.shields.io/badge/Formatter-black-black) ![my badge](https://badgen.net/badge/Createdby/RJA/black?icon=gitlab)

---

### Python Continuous Integration with GitHub Actions demo

This minimal example is to show how to setup a project directory for a python project
structuring:

- all the code under the python_actions directory, with each subdirectory being a package,
  and under it one or more module files, each containing one or more functions/classes
- Code is evaluated with pylint (pylint src)
- all the tests are under the tests directory to be picked up by pytest and each test imports the needed modules and functions.
- pytest will also perform a coverage test to be sent to Codecov
- the workflow automating all of this is in the .github/workflows directory and is triggered by a push to the master branch

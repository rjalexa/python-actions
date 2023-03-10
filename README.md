# python-test: a demo python repository with GitHub actions for code quality

## Live status:

[![Test workflow](https://github.com/rjalexa/python-actions/actions/workflows/python-test.yml/badge.svg)](https://github.com/rjalexa/python-actions/actions/workflows/python-test.yml) [![Codecov](https://codecov.io/gh/rjalexa/python-actions/branch/main/graph/badge.svg?token=1F2VGHFJ3S)](https://codecov.io/gh/rjalexa/python-test) ![Linting](https://github.com/rjalexa/python-actions/actions/workflows/python-lint.yml/badge.svg) [![Open issues](https://img.shields.io/github/issues/rjalexa/python-actions)](https://github.com/rjalexa/python-actions/issues)

## Tooling

[![linting: pylint](https://img.shields.io/badge/linting-pylint-black)](https://github.com/PyCQA/pylint) ![Formatter](https://img.shields.io/badge/Formatter-black-black) ![my badge](https://badgen.net/badge/Createdby/RJA/black?icon=gitlab)

---

### Python Continuous Integration with GitHub Actions demo

This minimal example is to show how to setup a python project directory, tooling and github actions to achieve an enforcement of code quality:

- all the code is laocated under the **python_actions** directory, with each subdirectory being a package, and under it one or more module files, each containing one or more functions/classes
- Code is formatted with **black** and linted with **pylint**
- all the tests are found under the **tests** directory to be picked up by **pytest** and each test imports the needed modules and functions.
- pytest with **pytest-cov** will also perform a coverage test to be sent to **Codecov**
- the workflows automating all of this are in the **.github/workflows** directory and are triggered by a **push** or by a **pull request** to the master branch.
- **pre-commit** hooks can run more or less the same checks on the local repository
- the only (local) prerequisites are **pyenv** and **poetry**
- **setup.cfg** contains parameter for mypy, pydantic and flake8
- **poetry.toml** contains options for poetry
- **pyproject.toml** contains options for

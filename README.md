# pylint-file-header

[![Pypi](https://img.shields.io/pypi/v/pylintfileheader.svg?style=flat-square)](https://pypi.python.org/pypi/pylintfileheader) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pylintfileheader.svg?style=flat-square)](https://pypi.python.org/pypi/pylintfileheader) [![PyPI - Downloads](https://img.shields.io/pypi/dm/pylintfileheader.svg?style=flat-square)](https://pypistats.org/packages/pylintfileheader) [![Stars](https://img.shields.io/github/stars/HaaLeo/pylint-file-header.svg?label=Stars&logo=github&style=flat-square)](https://github.com/HaaLeo/pylint-file-header/stargazers)  
[![PyPI - License](https://img.shields.io/pypi/l/pylintfileheader.svg?style=flat-square)](https://raw.githubusercontent.com/HaaLeo/pylint-file-header/master/LICENSE.txt) [![Build Status](https://img.shields.io/travis/HaaLeo/pylint-file-header/master.svg?style=flat-square)](https://travis-ci.org/HaaLeo/pylint-file-header) [![Codecov](https://img.shields.io/codecov/c/github/HaaLeo/pylint-file-header.svg?style=flat-square)](https://codecov.io/gh/HaaLeo/pylint-file-header) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  
[![Donate](https://img.shields.io/badge/-Donate-blue.svg?logo=paypal&style=flat-square)](https://www.paypal.me/LeoHanisch)

Pylint plugin to enforce consistent file/module header.

## Installation

You can install the package with `pip` from [pypi](https://pypi.org/project/pylintfileheader):

```
pip install pylintfileheader
```

## Configuration

Generate a `.pylintrc` file by executing `pylint --generate-rcfile`.
Then add `pylintfileheader` to the plugins to load and set the `file-header` option to the [regular expression](https://docs.python.org/3/library/re.html#regular-expression-syntax) that the file header should match.  
When the `file-header` setting is omitted, pylint will pass.

### Options

* `file-header` is a regexp representing the file header that should be on top of a file.
* `file-header-path` is the path to the file that contains the header. This is useful in case of long, multi-line headers, such as copyrights.
* `file-header-ignore-empty-files` turns on the mode of ignoring the empty files, like `__init__.py`. The default value is `False`.

If both options `file-header` and `file-header-path` are set, then `file-header` will be used and the `file-header-path` is ignored.

## Example

### Setup

* **.pylintrc**:  

  ```pylintrc
  [MASTER]
  load-plugins=pylintfileheader

  file-header=# -----------\n#[ \w]*\n# -----------
  ```

* **valid_example.py**:  

  ```python
  # -----------
  # lorem ipsum
  # -----------

  print('I am a valid example')
  ```

* **invalid_example.py**:  

  ```python
  # lorem ipsum

  print('I am an invalid example')
  ```

### Evaluation

* `pylint valid_example.py` evaluates to:  
  ```
  Using config file /path/to/your/.pylintrc

  ------------------------------------
  Your code has been rated at 10.00/10
  ```

* `pylint invalid_example.py` evaluates to:  
  ```
  Using config file /path/to/your/.pylintrc
  ************* Module invalid_example
  C:  1, 0: File header should match regex "# -----------\n#[ \w]*\n# -----------" (invalid-file-header)

  -----------------------------------
  Your code has been rated at 8.57/10
  ```

## Contribution

If you found a bug or are missing a feature do not hesitate to [file an issue](https://github.com/HaaLeo/pylint-file-header/issues/new/choose).  
Pull Requests are welcome!

## Support

When you like this package make sure to [star the repository](https://github.com/HaaLeo/pylint-file-header/stargazers). I am always looking for new ideas and feedback.  
In addition, it is possible to [donate via paypal](https://www.paypal.me/LeoHanisch).

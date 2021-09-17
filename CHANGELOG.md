# Changelog
All notable changes to the "pylintfileheader" pypi package will be documented in this file.  
This project follows [semantic versioning](https://semver.org/).

## Unreleased

[All Changes](https://github.com/HaaLeo/pylint-file-header/compare/v0.3.0...master)

## 2021-09-17 - [v0.3.2]
### Fixed
* pypi file upload

[All Changes](https://github.com/HaaLeo/pylint-file-header/compare/v0.3.1...v0.3.2)

## 2021-09-17 - [v0.3.1]
### Fixed
* how the file header and files are read. Now windows' CRLF line breaks are supported. Thx to Piotr Kasprzyk ([@pkasprzyk](https://github.com/pkasprzyk)).

[All Changes](https://github.com/HaaLeo/pylint-file-header/compare/v0.3.0...v0.3.1)

## 2020-12-28 - [v0.3.0](https://github.com/HaaLeo/pylint-file-header/tree/v0.3.0)

### Added
* option `file-header-path` to store the file header in its own file. Contributed by Sergey Vilgelm ([@SVilgelm](https://github.com/SVilgelm))

[All Changes](https://github.com/HaaLeo/pylint-file-header/compare/v0.2.0...v0.3.0)

## 2020-12-28 - [v0.2.0](https://github.com/HaaLeo/pylint-file-header/tree/v0.2.0)

### Added
* option `file-header-ignore-empty-files` to ignore empty files ([#1](https://github.com/HaaLeo/pylint-file-header/issues/1)) contributed by Sergey Vilgelm ([@SVilgelm](https://github.com/SVilgelm))

[All Changes](https://github.com/HaaLeo/pylint-file-header/compare/v0.1.0...v0.2.0)

## 2019-10-30 - [v0.1.0](https://github.com/HaaLeo/pylint-file-header/tree/v0.1.0)

### DEPRECATED
* python 2.7 support: The next major release will drop support for python 2.7

### Added
* [CI jobs](https://travis-ci.org/HaaLeo/pylint-file-header) to test against all supported python versions

[All Changes](https://github.com/HaaLeo/pylint-file-header/compare/v0.0.2...v0.1.0)

## 2018-11-28 - [v0.0.2](https://github.com/HaaLeo/pylint-file-header/tree/v0.0.2)

### Added
* [code coverage](https://codecov.io/gh/HaaLeo/pylint-file-header)

### Fixed
* example usage in the readme

[All Changes](https://github.com/HaaLeo/pylint-file-header/compare/v0.0.1...v0.0.2)

## 2018-11-25 - [v0.0.1](https://github.com/HaaLeo/pylint-file-header/tree/v0.0.1)

* **Initial Release**
### Added
* a feature that enables pylint to lint for a consistent file header

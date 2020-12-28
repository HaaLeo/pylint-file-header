# ---------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the MIT License. See LICENSE.txt in the project root for license information.
# ---------------------------------------------------------------------------------------------

# pylint: disable=invalid-name,unused-variable
import re
import sys

from mock import MagicMock
import pylint.testutils
import pytest

from pylintfileheader.file_header_checker import FileHeaderChecker


class TestFileHeaderChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = FileHeaderChecker
    CONFIG = {'file_header': '# Valid\n# Header'}

    def test_valid_header_no_message_added(self):
        """Test whether no message is added, when the file header is valid."""

        node_mock = MagicMock()
        node_mock.stream.return_value.__enter__.return_value.read.return_value.decode.return_value = '# Valid\n# Header'
        with self.assertNoMessages():
            self.checker.process_module(node_mock)

    def test_invalid_header_message_added(self):
        """Test whether no message is added, when the file header is valid."""

        node_mock = MagicMock()
        node_mock.stream.return_value.__enter__.return_value.read.return_value.decode.return_value = '# Invalid\n# Header'
        with self.assertAddsMessages(pylint.testutils.Message(
                msg_id='invalid-file-header',
                line=1,
                args='# Valid\n# Header')):
            self.checker.process_module(node_mock)

    def test_valid_header_not_at_top_message_added(self):
        """Test whether no message is added, when the file header is valid."""

        node_mock = MagicMock()
        node_mock.stream.return_value.__enter__.return_value.read.return_value.decode.return_value = 'print(\'hello\')\n# Valid\n# Header'
        with self.assertAddsMessages(pylint.testutils.Message(
                msg_id='invalid-file-header',
                line=1,
                args='# Valid\n# Header')):
            self.checker.process_module(node_mock)

    def test_ignore_empty_files(self):
        """When the `file-header-ignore-empty-files` option is set to True."""

        self.checker.config.file_header_ignore_empty_files = True
        node_mock = MagicMock()
        node_mock.stream.return_value.__enter__.return_value.read.return_value.decode.return_value = ''
        with self.assertNoMessages():
            self.checker.process_module(node_mock)

    def test_do_not_ignore_empty_files(self):
        """When the `file-header-ignore-empty-files` option is set to False (default value)."""

        node_mock = MagicMock()
        node_mock.stream.return_value.__enter__.return_value.read.return_value.decode.return_value = ''
        with self.assertAddsMessages(pylint.testutils.Message(
                msg_id='invalid-file-header',
                line=1,
                args='# Valid\n# Header')):
            self.checker.process_module(node_mock)


class TestFileHeaderCheckerNoConfig(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = FileHeaderChecker
    CONFIG = {}

    def test_no_message_added(self):
        """When the `file-header` option is not set, no message should be added."""

        node_mock = MagicMock()
        node_mock.stream.return_value.__enter__.return_value.read.return_value.decode.return_value = '# Invalid\n# Header'
        with self.assertNoMessages():
            self.checker.process_module(node_mock)


class TestFileHeaderCheckerPathMain(TestFileHeaderChecker):
    CHECKER_CLASS = FileHeaderChecker
    CONFIG = {'file_header_path': 'pylintfileheadertest/header.txt'}


class TestFileHeaderCheckerPathExtra:
    CHECKER_CLASS = FileHeaderChecker

    def get_checker(self, config):
        linter = pylint.testutils.UnittestLinter()
        checker = self.CHECKER_CLASS(linter)
        for key, value in config.items():
            setattr(checker.config, key, value)
        return checker

    def test_incorrect_regex(self):
        with pytest.raises(re.error):
            self.get_checker({
                'file_header': '.+)',
            }).open()

    def test_wrong_path(self):
        if sys.version_info[0] < 3:
            excp = IOError
        else:
            excp = FileNotFoundError

        with pytest.raises(excp):
            self.get_checker({
                'file_header_path': 'foo-bar.txt',
            }).open()

    def test_both_options(self):
        # no error expected since the file_header is used
        checker = self.get_checker({
            'file_header': '# Valid\n# Header',
            'file_header_path': 'foo-bar.txt',
        })
        checker.open()
        assert checker.header == '# Valid\n# Header'

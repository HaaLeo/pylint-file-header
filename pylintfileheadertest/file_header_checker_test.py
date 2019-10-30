# ---------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the MIT License. See LICENSE.txt in the project root for license information.
# ---------------------------------------------------------------------------------------------

# pylint: disable=invalid-name,unused-variable
from mock import MagicMock
import pylint.testutils
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

    def test_config_empty_no_message_added(self):
        """When the `file-header` option is not set, no message should be added."""

        self.checker.config.file_header = None
        node_mock = MagicMock()
        node_mock.stream.return_value.__enter__.return_value.read.return_value.decode.return_value = '# Invalid\n# Header'
        with self.assertNoMessages():
            self.checker.process_module(node_mock)

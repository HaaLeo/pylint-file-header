# ---------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the MIT License. See LICENSE.txt in the project root for license information.
# ---------------------------------------------------------------------------------------------
import re
import sys

from pylint.checkers import BaseChecker
from pylint.interfaces import IRawChecker

# pylint: disable=anomalous-backslash-in-string


class FileHeaderChecker(BaseChecker):
    __implements__ = IRawChecker

    name = 'pylintfileheader'

    msgs = {
        'C5001': (
            'File header must match regex "%s"',
            'invalid-file-header',
            'Used when the file header does not match the '
            'regex configured in the `file-header` option.'
        )
    }

    options = (
        (
            'file-header',
            {
                'default': None,
                'type': 'string',
                'metavar': '<REGEXP>',
                'help': 'The file header that should be on top of a file.',
            }
        ),
        (
            'file-header-path',
            {
                'default': None,
                'type': 'string',
                'metavar': '<file>',
                'help': 'The path to the file that contains the header.',
            }
        ),
        (
            'file-header-ignore-empty-files',
            {
                'default': False,
                'type': 'yn',
                'metavar': 'y_or_n',
                'help': 'Ignoring the empty files.',
            }
        ),
    )

    def __init__(self, linter=None):
        # pylint: disable=super-with-arguments
        super(FileHeaderChecker, self).__init__(linter=linter)
        self.pattern = None
        self.header = None

    def open(self):
        self.header = self.config.file_header
        if not self.header and self.config.file_header_path:
            with open(self.config.file_header_path, 'rb') as header_file:
                self.header = header_file.read().decode('utf-8')

        if self.header:
            if sys.version_info[0] < 3:
                opts = re.LOCALE | re.MULTILINE
            else:
                opts = re.MULTILINE
            self.pattern = re.compile(r'\A' + self.header, opts)

    def process_module(self, node):
        """Process the astroid node stream."""

        if self.pattern is None:
            return

        content = None
        with node.stream() as stream:
            # Explicit decoding required by python 3
            content = stream.read().decode('utf-8')

        if self.config.file_header_ignore_empty_files and not content:
            return

        matches = self.pattern.findall(content)

        if len(matches) != 1:
            self.add_message('invalid-file-header', 1, args=self.header)

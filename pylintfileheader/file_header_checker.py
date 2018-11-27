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
            'File header should match regex "%s"',
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
    )

    def process_module(self, node):
        """Process the astroid node stream."""
        if self.config.file_header:
            if sys.version_info[0] < 3:
                pattern = re.compile(
                    '\A' + self.config.file_header, re.LOCALE | re.MULTILINE)
            else:
                # The use of re.LOCALE is discouraged in python 3
                pattern = re.compile(
                    '\A' + self.config.file_header, re.MULTILINE)

            content = None
            with node.stream() as stream:
                # Explicit decoding required by python 3
                content = stream.read().decode('utf-8')

            matches = pattern.findall(content)

            if len(matches) != 1:
                self.add_message('invalid-file-header', 1,
                                 args=self.config.file_header)

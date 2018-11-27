# ---------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the MIT License. See LICENSE.txt in the project root for license information.
# ---------------------------------------------------------------------------------------------

"""Module which defines the required register method
for Pylint plugins.
"""

from pylintfileheader.file_header_checker import FileHeaderChecker


def register(linter):
    """Required method to auto register this checker.
    Args:
        linter: Main interface object for Pylint plugins.
    """
    linter.register_checker(FileHeaderChecker(linter))

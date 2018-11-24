from pylint.checkers import BaseChecker
from pylint.interfaces import IRawChecker


class FileHeaderChecker(BaseChecker):
    __implements__ = IRawChecker

    name = 'pylintfileheader'

    msgs = {
        'C5001': (
            'Invalid file header %s, should be %s',
            'invalid-file-header',
            'Used when the file header does not match the '
            'value configured in the `file-header` option.'
        )
    }

    options = (
        (
            'file-header',
            {
                'type': 'string',
                'default': None,
                'help': 'The file header that should be on top of a file.'
            }
        )
    )

    def process_module(self, astroid):
        print(astroid)

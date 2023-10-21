from antlr4.error.ErrorListener import ErrorListener
import codecs
from logging import getLogger
logger = getLogger(__name__)

class ATKRLErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = codecs.decode(msg, 'unicode_escape')
        logger.error(f'line {line}:{column} {msg}')
        exit(1)
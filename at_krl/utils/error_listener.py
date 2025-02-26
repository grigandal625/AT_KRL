import codecs
from logging import getLogger

from antlr4.error.ErrorListener import ErrorListener

logger = getLogger(__name__)


class ATKRLErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if "expecting '" in msg:
            index = msg.index("expecting '") + 11
            to_convert = msg[index:]
            msg = msg.replace(to_convert, "")
            to_convert = codecs.decode(to_convert, "unicode_escape")
            msg = msg + to_convert
        logger.error(f"line {line}:{column + 1} {msg}")

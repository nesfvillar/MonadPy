from monad import Monad
from traceback import extract_stack


class Result(Monad):
    def __init__(self, value, error=None):
        self._value = value
        self._error = error

    def bind(self, f):
        if self.isError():
            return self

        try:
            return super().bind(f)

        except Exception as e:
            error = {
                "exception": e,
                "trace": extract_stack(),
                "value": self.unwrap()
            }

            return Result(None, error)

    def isOk(self):
        return self._error is not None

    def isError(self):
        return not self.isOk()
    
    def getError(self):
        return self._error

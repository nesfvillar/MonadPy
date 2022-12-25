from monads.monad import Monad


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
                "value": self._value
            }

            return Result(self._value, error)

    def isOk(self):
        return self._error is None

    def isError(self):
        return not self.isOk()

    def getError(self):
        return self._error

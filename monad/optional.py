from monad import Monad


class Optional(Monad):
    def __init__(self, value):
        self._value = value

    def bind(self, f):
        return super().bind(f) if self.isJust() else self

    def isJust(self):
        return self.unwrap() is not None

    def isNone(self):
        return not self.isJust()

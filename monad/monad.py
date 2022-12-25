class Monad:
    def bind(self, f):
        return f(self._value)

    def unwrap(self):
        return self._value

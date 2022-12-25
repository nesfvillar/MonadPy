class Monad:
    def bind(self, f):
        return f(self._value)

    def unwrap(self):
        return self._value

    @classmethod
    def functionConvert(cls, func):
        return lambda *args, **kwargs: cls(func(*args, **kwargs))

class Monad:
    def bind(self, f):
        return f(self._value)

    def __rshift__(self, func):
        return self.bind(func)

    def unwrap(self):
        return self._value

    @classmethod
    def functionConvert(cls, func):
        return lambda *args, **kwargs: cls(func(*args, **kwargs))

    def __eq__(self, __monad):
        return self.unwrap() == __monad.unwrap()

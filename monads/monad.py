class Monad:
    def __init__(self, value):
        self._value = value

    def bind(self, *funcs):
        value = self
        for func in funcs:
            value = func(value.unwrap())
            if not issubclass(type(value), self.__class__):
                value = self.__class__(value)
        return value

    def unwrap(self):
        return self._value

    @classmethod
    def fnConvert(cls, func):
        return lambda *args, **kwargs: cls(func(*args, **kwargs))

    def __eq__(self, __monad):
        return self.unwrap() == __monad.unwrap()

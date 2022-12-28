class Monad:
    def __init__(self, value):
        self._value = value

    def bind(self, *funcs):
        monad = self
        for func in funcs:
            monad = func(monad.unwrap())
            if not issubclass(type(monad), self.__class__):
                monad = self.__class__(monad)
        return monad

    def unwrap(self):
        return self._value

    @classmethod
    def fnConvert(cls, func):
        return lambda *args, **kwargs: cls(func(*args, **kwargs))

    def __eq__(self, __monad):
        return self.unwrap() == __monad.unwrap()

    def __rshift__(self, __right):
        return self.bind(__right)

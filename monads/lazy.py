from monads.monad import Monad


class Lazy(Monad):
    def __init__(self, value, *funcs):
        super().__init__(value)
        self._funcs = funcs

    def bind(self, *funcs):
        return Lazy(self._value, *(self._funcs + funcs))

    def unwrap(self):
        value = super().unwrap()
        for func in self._funcs:
            value = func(value)
            if issubclass(type(value), Lazy):
                value = value.unwrap()
        return value

    @classmethod
    def fnConvert(cls, func):
        return lambda value: cls(value, func)

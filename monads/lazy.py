from monads.monad import Monad

from collections.abc import Callable


class Lazy(Monad):
    def __init__(self, value):
        if isinstance(value, Callable):
            super().__init__(value)
        else:
            super().__init__(lambda: value)

    def bind(self, *funcs):
        lazy = self
        for func in funcs:
            lazy = lazy._bind_help(func)

        return lazy

    def _bind_help(self, func):
        return Lazy(lambda: func(self.unwrap()))

    def unwrap(self):
        return super().unwrap()()

    @classmethod
    def fnConvert(cls, func):
        return func

from monads.monad import Monad


class Optional(Monad):
    def bind(self, *funcs):
        return super().bind(*funcs) if self.isJust() else self

    def isJust(self):
        return self.unwrap() is not None

    def isNothing(self):
        return not self.isJust()

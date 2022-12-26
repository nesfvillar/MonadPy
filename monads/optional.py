from monads.monad import Monad


class Optional(Monad):
    def bind(self, f):
        return super().bind(f) if self.isJust() else self

    def isJust(self):
        return self.unwrap() is not None

    def isNothing(self):
        return not self.isJust()

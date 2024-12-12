from typing import Callable, Protocol


class Functor[T](Protocol):
    def fmap[U](self, func: Callable[[T], U]) -> "Functor[U]": ...

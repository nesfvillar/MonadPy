from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Lazy[T]:
    _func: Callable[[], T]

    def fmap[U](self, func: Callable[[T], U]) -> "Lazy[U]":
        return Lazy(lambda: func(self._func()))

    def apply[U, V](self: "Lazy[Callable[[U], V]]", value: "Lazy[U]") -> "Lazy[V]":
        return value.fmap(self.unwrap())

    def bind[U](self, func: Callable[[T], "Lazy[U]"]) -> "Lazy[U]":
        return self.fmap(lambda x: func(x).unwrap())

    def unwrap(self) -> T:
        return self._func()

from monad import Monad

from typing import Any, Callable, List, TypeVar
from dataclasses import dataclass, field


A = TypeVar("A")
B = TypeVar("B")

@dataclass
class Lazy(Monad[A]):
    _value: Any
    _funcs: List[Callable[[Any], A]] = field(default_factory=list)

    def fmap(self, func: Callable[[A], B]) -> 'Lazy[B]':
        return Lazy(self._value, self._funcs + [func])

    def unwrap(self) -> A:
        value = self._value
        for func in self._funcs:
            value = func(value)
        return value

from typing import Any, Callable, Generic, List, TypeVar
from dataclasses import dataclass

A = TypeVar("A")
B = TypeVar("B")

@dataclass
class Lazy(Generic[A]):
    _value: Any
    _funcs: List[Callable[[Any], A]]

    def fmap(self, func: Callable[[A], B]) -> 'Lazy[B]':
        return Lazy(self._value, self._funcs + [func])

    def unwrap(self) -> A:
        value = self._value
        for func in self._funcs:
            value = func(value)
        return value

    def bind(self, func: Callable[[A], 'Lazy[B]']) -> 'Lazy[B]':
        ...

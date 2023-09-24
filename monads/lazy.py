from __future__ import annotations

from .monad import Monad

from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from functools import reduce
from itertools import chain
from typing import Any, TypeVar

A = TypeVar("A")
B = TypeVar("B")


@dataclass(frozen=True)
class Lazy(Monad[A]):
    _value: Any
    _funcs: Iterable[Callable[[Any], Any | A]] = field(default_factory=list)

    def fmap(self, func: Callable[[A], B]) -> Lazy[B]:
        return Lazy(self._value, chain(self._funcs, [func]))

    def unwrap(self) -> A:
        return reduce(lambda value, func: func(value), self._funcs, self._value)

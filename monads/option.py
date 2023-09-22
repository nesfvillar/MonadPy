from __future__ import annotations

from .functor import Functor
from .monad import Monad

from dataclasses import dataclass
from collections.abc import Callable
from typing import Any, Never, TypeVar

A = TypeVar("A")
B = TypeVar("B")


class Option(Monad[A]):
    ...


@dataclass(frozen=True)
class Some(Option[A]):
    _value: A

    def fmap(self, func: Callable[[A], B]) -> Option[B]:
        new_value = func(self._value)
        return Some(new_value)

    def unwrap(self) -> A:
        return self._value


class Nothing(Option[Any]):
    def fmap(self, func: Callable[[Any], Any]) -> Nothing:
        return self

    def apply(self, value: Functor[Any]) -> Nothing:
        return self

    def unwrap(self) -> Never:
        raise ValueError("Unwrapped a Nothing value")

    def bind(self, func: Callable[[Any], Monad[Any]]) -> Nothing:
        return self

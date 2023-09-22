from __future__ import annotations

from .functor import Functor
from .monad import Monad

from dataclasses import dataclass
from typing import Any, Callable, Never, TypeVar


A = TypeVar("A")
B = TypeVar("B")

class Result(Monad[A]):
    ...


@dataclass(frozen=True)
class Ok(Result[A]):
    _value: A

    def fmap(self, func: Callable[[A], B]) -> Result[B]:
        try:
            new_value = func(self._value)
            return Ok(new_value)
        except Exception as err:
            return Err(err)

    def unwrap(self) -> A:
        return self._value


@dataclass(frozen=True)
class Err(Result[Any]):
    _error: Exception

    def fmap(self, func: Callable[[Any], Any]) -> Err:
        return self

    def apply(self, value: Functor[Any]) -> Err:
        return self

    def unwrap(self) -> Never:
        raise self._error

    def bind(self, func: Callable[[Any], Monad[Any]]) -> Err:
        return self

from functor import Functor
from monad import Monad

from typing import Any, Callable, TypeVar
from dataclasses import dataclass


A = TypeVar("A")
B = TypeVar("B")

class Optional(Monad[A]):
    ...


@dataclass(frozen=True)
class Some(Optional[A]):
    _value: A

    def fmap(self, func: Callable[[A], B]) -> Optional[B]:
        try:
            new_value = func(self._value)
            return Some(new_value)
        except Exception:
            return Nothing()

    def unwrap(self) -> A:
        return self._value


class Nothing(Optional[Any]):
    def fmap(self, func: Callable[[Any], Any]) -> 'Nothing':
        return self

    def apply(self, value: Functor[Any]) -> 'Nothing':
        return self

    def unwrap(self) -> None:
        raise ValueError("Unwrapped a Nothing value")

    def bind(self, func: Callable[[Any], Monad[Any]]) -> 'Nothing':
        return self

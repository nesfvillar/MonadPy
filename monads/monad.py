from __future__ import annotations

from .applicative import Applicative
from .functor import Functor

from abc import abstractmethod
from collections.abc import Callable
from typing import TypeVar

A = TypeVar("A")
B = TypeVar("B")
F = TypeVar("F", bound=Functor)
M = TypeVar("M", bound='Monad')


class Monad(Applicative[A]):
    @abstractmethod
    def unwrap(self) -> A:
        ...

    # def apply(self: Monad[Callable[[A], B]], value: F[B]) -> F[B]:
    def apply(self: Monad[Callable[[A], B]], value: F) -> F:
        func = self.unwrap()
        return value.fmap(func)

    # def bind(self, func: Callable[[A], M[B]]) -> M[B]:
    def bind(self, func: Callable[[A], M]) -> M:
        value = self.unwrap()
        return func(value)

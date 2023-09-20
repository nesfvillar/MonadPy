from applicative import Applicative
from functor import Functor

from abc import ABC, abstractmethod
from typing import Callable, TypeVar


A = TypeVar("A")
B = TypeVar("B")

class Monad(Applicative[A], ABC):
    @abstractmethod
    def unwrap(self) -> A:
        ...

    def apply(self: 'Monad[Callable[[A], B]]', value: Functor[A]) -> Functor[B]:
        func = self.unwrap()
        return value.fmap(func)

    def bind(self, func: Callable[[A], 'Monad[B]']) -> 'Monad[B]':
        value = self.unwrap()
        return func(value)

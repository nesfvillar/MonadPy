from functor import Functor

from abc import ABC, abstractmethod
from typing import Callable, TypeVar


A = TypeVar("A")
B = TypeVar("B")

class Monad(Functor[A], ABC):
    @abstractmethod
    def unwrap(self) -> A:
        ...

    def bind(self, func: Callable[[A], 'Monad[B]']) -> 'Monad[B]':
        value = self.unwrap()
        return func(value)

from functor import Functor

from abc import ABC, abstractmethod
from typing import Callable, TypeVar

A = TypeVar("A")
B = TypeVar("B")

class Applicative(Functor[A], ABC):
    @abstractmethod
    def apply(self: Functor[Callable[[A], B]], value: Functor[A]) -> Functor[B]:
        ...

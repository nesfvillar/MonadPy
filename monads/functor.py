from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar


A = TypeVar("A")
B = TypeVar("B")

class Functor(Generic[A], ABC):
    @abstractmethod
    def fmap(self, func: Callable[[A], B]) -> 'Functor[B]':
        ...
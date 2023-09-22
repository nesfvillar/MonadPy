from __future__ import annotations

from abc import abstractmethod
from typing import Callable, Generic, TypeVar


A = TypeVar("A")
B = TypeVar("B")

class Functor(Generic[A]):
    @abstractmethod
    def fmap(self, func: Callable[[A], B]) -> Functor[B]:
        ...

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Generic, TypeVar

A = TypeVar("A")
B = TypeVar("B")


class Functor(ABC, Generic[A]):
    @abstractmethod
    def fmap(self, func: Callable[[A], B]) -> Functor[B]:
        ...

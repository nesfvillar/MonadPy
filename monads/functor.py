from typing import Callable, TypeVar, Protocol

A = TypeVar("A")
B = TypeVar("B")

class Functor(Protocol[A]):
    def fmap(self, func: Callable[[A], B]) -> 'Functor[B]':
        ...
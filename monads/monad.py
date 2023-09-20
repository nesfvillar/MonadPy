from typing import Callable, TypeVar, Protocol

A = TypeVar("A")
B = TypeVar("B")

class Monad(Protocol[A]):
    def unwrap(self) -> A:
        ...

    def bind(self, func: Callable[[A], 'Monad[B]']) -> 'Monad[B]':
        ...
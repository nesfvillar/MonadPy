from typing import Any, Callable, Generic, TypeVar
from dataclasses import dataclass
from abc import ABC, abstractmethod

A = TypeVar("A")
B = TypeVar("B")

class Optional(Generic[A], ABC):

    @abstractmethod
    def fmap(self, func: Callable[[A], B]) -> 'Optional[B]':
        ...

    @abstractmethod
    def unwrap(self) -> A:
        ...

    @abstractmethod
    def bind(self, func: Callable[[A], 'Optional[B]']) -> 'Optional[B]':
        ...


@dataclass
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

    def bind(self, func: Callable[[A], Optional[B]]) -> Optional[B]:
        return func(self._value)


class Nothing(Optional[Any]):
    def fmap(self, func: Callable[[Any], B]) -> Optional[B]:
        return self

    def unwrap(self) -> None:
        raise ValueError("Unwraped a Nothing value")

    def bind(self, func: Callable[[Any], Optional[B]]) -> Optional[B]:
        return self



from typing import Any, Callable, Generic, TypeVar
from dataclasses import dataclass
from abc import ABC, abstractmethod

A = TypeVar("A")
B = TypeVar("B")


class Result(Generic[A], ABC):
    @abstractmethod
    def fmap(self, func: Callable[[A], B]) -> 'Result[B]':
        ...

    @abstractmethod
    def unwrap(self) -> A:
        ...

    @abstractmethod
    def bind(self, func: Callable[[A], 'Result[B]']) -> 'Result[B]':
        ...


@dataclass
class Ok(Result[A]):
    _value: A

    def fmap(self, func: Callable[[A], B]) -> Result[B]:
        try:
            new_value = func(self._value)
            return Ok(new_value)
        except Exception as err:
            return Err(err)

    def unwrap(self) -> A:
        return self._value

    def bind(self, func: Callable[[A], Result[B]]) -> Result[B]:
        return func(self._value)


@dataclass
class Err(Result[Any]):
    _error: Exception

    def fmap(self, func: Callable[[Any], B]) -> Result[B]:
        return self

    def unwrap(self) -> Any:
        raise self._error

    def bind(self, func: Callable[[Any], Result[B]]) -> Result[B]:
        return self
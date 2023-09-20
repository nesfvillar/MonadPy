from monad import Monad

from typing import Any, Callable, TypeVar
from dataclasses import dataclass


A = TypeVar("A")
B = TypeVar("B")

class Result(Monad[A]):
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


@dataclass
class Err(Result[Any]):
    _error: Exception

    def fmap(self, func: Callable[[Any], B]) -> Result[B]:
        return self

    def unwrap(self) -> Any:
        raise self._error

    def bind(self, func: Callable[[Any], Result[B]]) -> Result[B]:
        return self

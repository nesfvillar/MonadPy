from dataclasses import dataclass
from typing import Any, Callable, Never, TypeVar, Union

_T = TypeVar("_T")
_U = TypeVar("_U")
Result = Union["Ok[_T]", "Err[_U]"]


@dataclass(frozen=True)
class Ok[T]:
    _value: T

    def fmap[U](self, func: Callable[[T], U]) -> Result[U, Exception]:
        try:
            return Ok(func(self._value))
        except Exception as err:
            return Err(err)

    def apply[U, V](
        self: "Ok[Callable[[U], V]]", value: Result[U, Any]
    ) -> Result[V, Any]:
        return value.fmap(self.unwrap())

    def bind[U](self, func: Callable[[T], Result[U, Any]]) -> Result[U, Any]:
        return func(self._value)

    def unwrap(self) -> T:
        return self._value


@dataclass(frozen=True)
class Err[T]:
    _value: Exception

    def fmap(self, _: Callable[[Any], Any]) -> "Err[T]":
        return self

    def apply(self, _: Result[Any, Any]) -> "Err[T]": ...

    def bind(self, _: Callable[[Any], Result[Any, Any]]) -> "Err[T]":
        return self

    def unwrap(self) -> Never:
        raise self._value

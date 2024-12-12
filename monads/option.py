from dataclasses import dataclass
from typing import Any, Callable, Never, TypeVar, Union

_T = TypeVar("_T")
Option = Union["Some[_T]", "Nothing"]


@dataclass(frozen=True)
class Some[T]:
    _value: T

    def fmap[U](self, func: Callable[[T], U]) -> Option[U]:
        try:
            return Some(func(self._value))
        except Exception:
            return Nothing()

    def apply[U, V](self: "Some[Callable[[U], V]]", value: Option[U]) -> Option[V]:
        return value.fmap(self.unwrap())

    def bind[U](self, func: Callable[[T], Option[U]]) -> Option[U]:
        return func(self._value)

    def unwrap(self) -> T:
        return self._value


class Nothing:
    def fmap(self, _: Callable[[Any], Any]) -> "Nothing":
        return self

    def apply(self, _: Option[Any]) -> "Nothing":
        return self

    def bind(self, _: Callable[[Any], Option[Any]]) -> "Nothing":
        return self

    def unwrap(self) -> Never:
        raise ValueError("Unwrapped a Nothing type")

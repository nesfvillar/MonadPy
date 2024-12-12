from typing import Callable, Protocol


class Monad[T](Protocol):
    def bind[U](self, func: Callable[[T], "Monad[U]"]) -> "Monad[U]": ...

    def unwrap(self) -> T: ...

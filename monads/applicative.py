from typing import Protocol


class Applicative[T](Protocol):
    def apply[U](self, value: "Applicative[T]") -> "Applicative[U]": ...

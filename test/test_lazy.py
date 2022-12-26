from unittest import TestCase
from monads.lazy import Lazy


class TestResult(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.lazy = Lazy("Hello world!")

    def test_unwrap(self):
        self.assertEqual("Hello world!", self.lazy.unwrap())

    def test_bind(self):
        self.assertListEqual(["hello", "world!"],
                             self.lazy.bind(str.lower, str.split).unwrap())

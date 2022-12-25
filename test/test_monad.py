from unittest import TestCase
from monads.optional import Optional


class TestResult(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.monad = Optional(5)

    def test_bind(self):
        self.assertEqual(Optional(6),
                         self.monad.bind(lambda x: Optional(x + 1)))

    def test_unwrap(self):
        self.assertEqual(5, self.monad.unwrap())

    def test___rshift__(self):
        self.assertEqual(Optional(6),
                         self.monad >> (lambda x: Optional(x + 1)))

    def test_functionConvert(self):
        @Optional.functionConvert
        def addOne(x):
            return x + 1

        self.assertEqual(Optional(6), self.monad >> addOne)

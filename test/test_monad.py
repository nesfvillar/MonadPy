from unittest import TestCase
from monads.optional import Optional


class TestResult(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.monad = Optional(5)

    def test_bind(self):
        @Optional.fnConvert
        def addOne(x):
            return x + 1

        self.assertEqual(Optional(7), self.monad.bind(addOne, addOne))

    def test_unwrap(self):
        self.assertEqual(5, self.monad.unwrap())

    def test_fnConvert(self):
        @Optional.fnConvert
        def addOne(x):
            return x + 1

        self.assertEqual(Optional(6), self.monad.bind(addOne))

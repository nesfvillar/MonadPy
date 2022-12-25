from unittest import TestCase
from monads.optional import Optional


class TestResult(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.justs = [Optional(5), Optional(0), Optional(""), Optional("None")]
        self.nones = [Optional(None)]

    def test_isJust(self):
        self.assertTrue(all(just.isJust() for just in self.justs))
        self.assertFalse(any(none.isJust() for none in self.nones))

    def test_isNothing(self):
        self.assertTrue(all(none.isNothing() for none in self.nones))
        self.assertFalse(any(just.isNothing() for just in self.justs))

    def test_unwrap(self):
        self.assertListEqual([5, 0, "", "None"], [just.unwrap()
                             for just in self.justs])
        self.assertListEqual([None], [none.unwrap() for none in self.nones])

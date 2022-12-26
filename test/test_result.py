from unittest import TestCase
from monads.result import Result


class TestResult(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.oks = [
            Result(5),
            Result({"Hello": "World"})
        ]
        self.errors = [
            Result(None, {"Error": 404}),
            Result("Seven", {"Custom": "Error"})
        ]

    def test_isOk(self):
        self.assertTrue(all(ok.isOk() for ok in self.oks))
        self.assertFalse(any(error.isOk() for error in self.errors))

    def test_isError(self):
        self.assertTrue(all(error.isError() for error in self.errors))
        self.assertFalse(any(ok.isError() for ok in self.oks))

    def test_getError(self):
        self.assertListEqual([{}, {}], [ok.getError() for ok in self.oks])
        self.assertListEqual([{"Error": 404}, {"Custom": "Error"}], [
                             error.getError() for error in self.errors])

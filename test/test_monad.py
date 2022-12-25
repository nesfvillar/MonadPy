from unittest import TestCase
from monads.optional import Optional


class TestResult(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.justs = [Optional(5), Optional(0), Optional(""), Optional("None")]

    def test_bind(self):
        ...

    def test_unwrap(self):
        ...

    def test_functionConvert(self):
        ...

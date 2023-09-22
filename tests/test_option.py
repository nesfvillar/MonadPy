from monads import *

import unittest


class TestSome(unittest.TestCase):
    s = Some('5')

    def test_fmap(self):
        i = self.s.fmap(int)
        self.assertEqual(i, Some(5))

    def test_unwrap(self):
        self.assertEqual(self.s.unwrap(), '5')

    def test_apply(self):
        f = Some(lambda s: s + 'World!')
        result = f.apply(self.s)
        self.assertEqual(result, Some('5World!'))

    def test_bind(self):
        def f(s): return Some(s + 'World!')
        result = self.s.bind(f)
        self.assertEqual(result, Some('5World!'))


class TestNothing(unittest.TestCase):
    def test_fmap(self):
        ...

    def test_unwrap(self):
        ...

    def test_apply(self):
        ...

    def test_bind(self):
        ...


if __name__ == '__main__':
    unittest.main()

import unittest

from icicle import FrozenDict

class FrozenDictTest(unittest.TestCase):

    def test_create_from_dict(self):
        d = {'a': 1, 'b': 2}
        fd = FrozenDict(d)
        self.assertEqual(fd['a'], 1)
        self.assertEqual(fd['b'], 2)

    def test_convert_to_dict(self):
        fd = FrozenDict(a=1, b=2)
        d = dict(fd)
        self.assertEqual(d, {'a': 1, 'b': 2})

    def test_immutable(self):
        fd = FrozenDict(a=1)
        with self.assertRaises(TypeError) as context:
            fd['a'] = 2
        message = "'FrozenDict' object does not support item assignment"
        self.assertIn(message, context.exception.message)

    def test_getitem(self):
        fd = FrozenDict(a=1, b=2)
        self.assertEqual(fd['a'], 1)
        self.assertEqual(fd['b'], 2)

    def test_iter(self):
        d = {'a': 1, 'b': 2}
        fd = FrozenDict(d)
        self.assertEqual(list(iter(d)), list(iter(fd)))

    def test_len(self):
        fd = FrozenDict(a=1, b=2, c=3)
        self.assertEqual(len(fd), 3)

    def test_hash(self):
        fd = FrozenDict(a=1, b=2, c=3)
        h = hash(fd)
        self.assertIsInstance(h, int)

    def test_repr(self):
        fd = FrozenDict(a=1, b=2, c=3)
        self.assertEqual(repr(fd), "FrozenDict({'a': 1, 'b': 2, 'c': 3})")

    def test_contains(self):
        fd = FrozenDict(a=1)
        self.assertIn('a', fd)
        self.assertNotIn('b', fd)

    def test_keys(self):
        fd = FrozenDict(a=1, b=2, c=3)
        self.assertEqual(sorted(fd.keys()), ['a', 'b', 'c'])

    def test_items(self):
        fd = FrozenDict(a=1, b=2, c=3)
        self.assertEqual(sorted(fd.items()), [('a', 1), ('b', 2), ('c', 3)])

    def test_values(self):
        fd = FrozenDict(a=1, b=2, c=3)
        self.assertEqual(sorted(fd.values()), [1, 2, 3])

    def test_get(self):
        fd = FrozenDict(a=1)
        self.assertEqual(fd.get('a', None), 1)
        self.assertEqual(fd.get('b', None), None)

    def test_eq(self):
        fd1 = FrozenDict(a=1, b=2)
        fd2 = FrozenDict(a=1, b=2)
        self.assertEqual(fd1, fd2)

    def test_ne(self):
        fd1 = FrozenDict(a=1, b=2, c=3)
        fd2 = FrozenDict(c=3, d=4)
        self.assertNotEqual(fd1, fd2)

if __name__ == '__main__':
    unittest.main()

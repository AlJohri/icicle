import unittest

from icicle import FrozenDict

class FrozenDictTest(unittest.TestCase):

  def test_create_from_dict(self):
    d = {'a': 1, 'b': 2}
    fd = FrozenDict(d)
    self.assertEquals(fd['a'], 1)
    self.assertEquals(fd['b'], 2)

  def test_convert_to_dict(self):
    fd = FrozenDict(a=1, b=2)
    d = dict(fd)
    self.assertEquals(d, {'a': 1, 'b': 2})

  def test_immutable(self):
    fd = FrozenDict(a=1)
    with self.assertRaises(TypeError) as context:
      fd['a'] = 2
    message = "'FrozenDict' object does not support item assignment"
    self.assertIn(message, context.exception.message)

if __name__ == '__main__':
  unittest.main()

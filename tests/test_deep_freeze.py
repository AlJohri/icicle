import unittest

from icicle import deep_freeze, FrozenDict

class DeepFreezeTest(unittest.TestCase):

  # same as freeze for non-container classes (rely on freeze?)
  def test_items(self):
    pass

  # dict parent, list parent, set parent
  def test_list_container(self):
    l = [[1], set([2, 3]), {4: 4}]
    t = ((1,), frozenset([2, 3]), FrozenDict({4: 4}))
    self.assertEquals(deep_freeze(l), t)

  def test_set_container(self):
    s = set([(1,), frozenset([2, 3]), FrozenDict({4: 4})])
    fs = frozenset([(1,), frozenset([2, 3]), FrozenDict({4: 4})])
    self.assertEquals(deep_freeze(s), fs)

  def test_dict_container(self):
    d = {1: [2,3]}
    fd = FrozenDict({1: (2, 3)})
    self.assertEquals(deep_freeze(d), fd)
  # bytearray parent?? i don't think so

if __name__ == '__main__':
  unittest.main()

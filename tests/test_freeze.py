import unittest

from icicle import freeze, FrozenDict

# ALREADY_IMMUTABLE = frozenset([
# ])
#
# TO_IMMUTABLE = FrozenDict({
#   dict: FrozenDict # mappings
# })

class FreezeTest(unittest.TestCase):

  def test_None(self):
    self.assertEquals(freeze(None), None)

  def test_numeric(self):
    self.assertEquals(freeze(1), 1) # int
    self.assertEquals(freeze(1L), 1L) # long
    self.assertEquals(freeze(1.0), 1.0) # float
    self.assertEquals(freeze(1.0), 1.0) # float
    self.assertEquals(freeze(complex(1,2)), complex(1,2)) # float

  def test_sequence(self):

    # immutables
    for immutable_sequence in (
      'hello world', unicode('hello world'),
      bytes([1, 2, 3]), (1, 2, 3)
    ):
      self.assertEquals(freeze(immutable_sequence), immutable_sequence)

    # mutables
    self.assertEquals(freeze(bytearray(['a', 'b', 'c'])), 'abc')
    self.assertEquals(freeze([1, 2, 3]), tuple([1, 2, 3]))

  ## Set
  def test_set(self):
    self.assertEquals(freeze(frozenset([1,2,3])), frozenset([1,2,3]))
    self.assertEquals(freeze(set([1,2,3])), frozenset([1,2,3]))

  ## Mapping
  def test_mapping(self):
    self.assertEquals(freeze({'a': 1, 'b': 2}), FrozenDict(a=1, b=2))

if __name__ == '__main__':
  unittest.main()

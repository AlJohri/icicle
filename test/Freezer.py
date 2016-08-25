import unittest

from icicle import Freezer

class Foo(object):
  def __init__(self, foo=None, **kwargs):
    if foo:
      self.d = dict(foo.d)
    else:
      self.d = dict(**kwargs)

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

class FrozenFoo(object):
  def __init__(self, foo=None, **kwargs):
    if foo:
      self.d = dict(foo.d)
    else:
      self.d = dict(**kwargs)

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

class FreezerTest(unittest.TestCase):
  # custom item type
  def test_item(self):

    obj = Foo(a=1)
    freezer = Freezer({Foo: FrozenFoo})
    self.assertEquals(freezer.freeze(obj), FrozenFoo(a=1))

  # custom container type
  def test_container(self):
    pass

if __name__ == '__main__':
  unittest.main()

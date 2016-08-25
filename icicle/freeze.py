import collections
from icicle import FrozenDict

# TODO buffer?
ALREADY_IMMUTABLE = frozenset([
  type(None), # NoneType
  int, long, float, complex, # numeric types
  str, unicode, bytes, tuple, # sequences
  frozenset, # sets
  FrozenDict # mappings
])

# type -> transform function
TO_IMMUTABLE = FrozenDict({
  bytearray: str, list: tuple, # sequences
  set: frozenset, # sets
  dict: FrozenDict # mappings
})

class Freezer(object):

  def __init__(self, immutable_transforms={}):
    self.immutable_transforms = immutable_transforms

  def freeze(self, obj):
    t = type(obj)
    if t in self.immutable_transforms:
      return self.immutable_transforms[t](obj)
    elif t in ALREADY_IMMUTABLE:
      return obj
    elif t in TO_IMMUTABLE:
      return TO_IMMUTABLE[t](obj)
    else:
      raise ValueError("type '{}' has no immutable counter-part".format(t))

  def deep_freeze(self, obj):
    '''Deep immutable copy of the object (recursively makes immutable copies).'''
    if not isinstance(obj, collections.Iterable):
      return freeze(obj)

    # list, set, dict
    items = tuple(deep_freeze(child) for child in obj)
    if isinstance(obj, dict) or isinstance(obj, FrozenDict):
      items = [(k, deep_freeze(v)) for k,v in obj.iteritems()]

    t = type(obj)
    # TODO check for custom transform??
    if t in self.immutable_transforms:
      # TODO what about children?
      items = self.children[t](obj)
      return self.immutable_transforms[t](items)
    elif t in ALREADY_IMMUTABLE:
      return t(items)
    elif t in TO_IMMUTABLE:
      return TO_IMMUTABLE[t](items)
    else:
      raise ValueError("type '{}' has no immutable counter-part".format(t))

DEFAULT_FREEZER = Freezer()

def freeze(obj):
  return DEFAULT_FREEZER.freeze(obj)

def deep_freeze(obj):
  return DEFAULT_FREEZER.deep_freeze(obj)

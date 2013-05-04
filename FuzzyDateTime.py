import datetime

class FuzzyDateTime(datetime.datetime):
  def __new__(cls, fuzzy_threshold=0, *args, **kwargs):
    val = super(FuzzyDateTime, cls).__new__(cls, *args, **kwargs)
    val.fuzzy_threshold = fuzzy_threshold
    return val

  def __cmp__(self, other):
    first, second = self, other
    if abs((first - second).total_seconds()) <= self.fuzzy_threshold:
      return 0
    elif super(FuzzyDateTime, self).__lt__(second):
      return -1
    elif super(FuzzyDateTime, self).__gt__(second):
      return 1
    raise "Never should have gotten here. Fix this edge case. Well, hopefully it's an edge case."
 

  def __lt__(self, other):
    return self.__cmp__(other) == -1
  def __gt__(self, other):
    return self.__cmp__(other) == 1
  def __eq__(self, other):
    return self.__cmp__(other) == 0

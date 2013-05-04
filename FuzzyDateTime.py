import datetime

"""
Implements fuzzy comparison for the DateTime object.
If two datetime objects are within a particular threshold
(specified as part of the constructror) they will be
treated as being equal. If two FuzzyDatetime objects
have different thresholds, the first one in the comparison
will have its threshold used.

Identical to standard datetime in all other ways.

Usage Example:

  seconds_threshold = 120
  first = FuzzyDateTime(seconds_threshold, 2013, 8, 12, 4, 1)
  second = FuzzyDateTime(seconds_threshold, 2013, 8, 12, 5, 10)
  first < second # This will evaluate to false since they're within
  two minutes (120 seconds) of each other
"""
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

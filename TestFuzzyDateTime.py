from FuzzyDateTime import FuzzyDateTime
import unittest

'''
Trying something new here- 
Naming date and time variables in tests is really obnoxious and 
weirdly abstract if you're trying to be descriptive. To make it easier to
reason about, I'm going to name this after presidents/historical figures 
who we "know", intuitively, are near and far from each other in history.
'''
class FuzzyDateTimeTestCase(unittest.TestCase):
  def setUp(self):
    t = 60*60*24*265*10 # 10 years
    self.lincoln = FuzzyDateTime(t, 1886, 1, 1, 0)
    self.grant = FuzzyDateTime(t, 1892, 1, 1, 0)
    self.clinton = FuzzyDateTime(t, 2000, 1,1,0)

  def testFuzzyLessReturnsTrueWhenSayingLincolnIsOlderThanClinton(self):
    self.assertTrue(self.lincoln < self.clinton)
  
  def testFuzzyLessReturnsFalseWhenSayingLincolnIsOlderThanGrant(self):
    self.assertFalse(self.lincoln < self.grant)

  def testFuzzyGreaterReturnsTrueWhenSayingClintonIsNewerThanGrant(self):
    self.assertTrue(self.clinton > self.grant)

  def testFuzzyGreaterReturnsFalseWhenSayingGrantIsNewerThanLincoln(self):
    self.assertFalse(self.grant > self.lincoln)

  def testFuzzyEqualsReturnsTrueWhenSayingGrantIsEqualToLincoln(self):
    self.assertTrue(self.grant == self.lincoln)

if __name__ == "__main__": 
  unittest.main()

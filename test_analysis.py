import unittest
from analysis import *
class Tests(unittest.TestCase):
    def test_model(self):
        self.assertAlmostEqual(sum(update(PRIOR,'bet').values()),1)
        self.assertAlmostEqual(update(PRIOR,'bet')['strong'],.16/.42)
        self.assertEqual(call_ev(0,100,50),-50)
if __name__=='__main__': unittest.main()

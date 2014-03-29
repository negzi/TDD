import unittest
import bowling

class BowlingTest(unittest.TestCase):

    def test_first(self):
        pinHits = [[2,6],[[0,0]]*9]
        self.assertAlmostEquals(8, bowling.BowlingClass().calculate_points(pinHits))

    def test_2(self):
        pinHits = [0, 0]
        self.assertAlmostEquals(0, bowling.BowlingClass().calculate_points(pinHits))

    def test_3(self):
        pinHits = [[2, 0], [5, 0]]
        self.assertAlmostEquals(9, bowling.BowlingClass().calculate_points(pinHits))


if __name__ == '__main__':
    unittest.main()
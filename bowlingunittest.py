import unittest
import bowling

class BowlingTest(unittest.TestCase):

    def test_first(self):
        pinHits = [[2,6]]+[[0,0]]*9
        self.assertAlmostEquals(8, bowling.BowlingClass().calculate_points(pinHits))

    def test_2(self):
        pinHits = [[0, 0]]
        self.assertAlmostEquals(0, bowling.BowlingClass().calculate_points(pinHits))

    def test_3(self):
        pinHits = [[2, 0], [5, 0]]
        self.assertAlmostEquals(7, bowling.BowlingClass().calculate_points(pinHits))

    def test_spares(self):
        pinHits = [[5, 5], [5, 0]]
        self.assertAlmostEquals(20, bowling.BowlingClass().calculate_points(pinHits))

    def test_spares2(self):
        pinHits = [[5, 5], [5, 0], [3,7],[1, 0]]
        self.assertAlmostEquals(32, bowling.BowlingClass().calculate_points(pinHits))

    def test_spares3(self):
        pinHits = [[10, 0], [5, 1]] +[[0,0]]*8
        self.assertAlmostEquals(22, bowling.BowlingClass().calculate_points(pinHits))

    def test_strikes1(self):
        pinHits = [[10, 0], [10, 0], [10, 0]] +[[0,0]]*7
        self.assertAlmostEquals(60, bowling.BowlingClass().calculate_points(pinHits))


if __name__ == '__main__':
    unittest.main()
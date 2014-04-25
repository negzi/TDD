import unittest
import bowling

class BowlingTest(unittest.TestCase):

    def test_first(self):
        pinHits = [[2,6]]+[[0,0]]*9
        self.assertEqual(8, bowling.Game().calc_score(pinHits))

    def test_2(self):
        pinHits = [[0, 0]]
        self.assertEqual(0, bowling.Game().calc_score(pinHits))

    def test_3(self):
        pinHits = [[2, 0], [5, 0]]
        self.assertEqual(7, bowling.Game().calc_score(pinHits))

    def test_spares(self):
        pinHits = [[5, 5], [5, 0]]
        self.assertEqual(20, bowling.Game().calc_score(pinHits))

    def test_spares2(self):
        pinHits = [[5, 5], [5, 0], [3,7],[1, 0]]
        self.assertEqual(32, bowling.Game().calc_score(pinHits))

    def test_spares3(self):
        pinHits = [[10, 0], [5, 1]] +[[0,0]]*8
        self.assertEqual(22, bowling.Game().calc_score(pinHits))

    def test_strikes1(self):
        pinHits = [[10, 0], [10, 0], [10, 0]] +[[0,0]]*7
        self.assertEqual(60, bowling.Game().calc_score(pinHits))

    def test_spares4(self):
        pinHits = [[0, 0]]*9 +[[9,1],[2,0]]
        self.assertEqual(12, bowling.Game().calc_score(pinHits))

    def test_strike2(self):
        pinHits = [[0, 0]]*9+ [[10, 0], [10, 0], [10, 0]]
        self.assertEqual(30, bowling.Game().calc_score(pinHits))

    def test_score_of_next_2_balls(self):
        pinHits = [[0,0],[10,0], [10, 0]]
        current_frame = 0
        self.assertEqual(20, bowling.Game().get_bonus(current_frame, pinHits))

    def test_score_of_next_2_balls2(self):
        pinHits = [[0,0],[5,3]]
        current_frame = 0
        self.assertEqual(8, bowling.Game().get_bonus(current_frame, pinHits))

    def test_strike4(self):
        pinHits = [[0, 0]]*9+ [[10, 0], [2, 1]]
        self.assertEqual(13, bowling.Game().calc_score(pinHits))

    def test_gutter_game(self):
        pinHits = [[0, 0]]*10
        self.assertEqual(0, bowling.Game().calc_score(pinHits))

    def test_perfect_game(self):
        pinHits = [[10, 0]]*12
        self.assertEqual(300, bowling.Game().calc_score(pinHits))






if __name__ == '__main__':
    unittest.main()

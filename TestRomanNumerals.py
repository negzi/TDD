import unittest
import RomanNumerals

class TestRomanNumerals(unittest.TestCase):

    obj = RomanNumerals.RomanNumerals()

    def test_one(self):
        '''simple example to start you off'''
        input = 1
        self.assertEqual('I', self.obj.answer(input))

    def test_two(self):
        self.assertEqual('II', self.obj.answer(2))

    def test_3(self):
        input = 3
        self.assertEqual('III', self.obj.answer(input))

    def test_4(self):
        input = 4
        self.assertEqual('IV', self.obj.answer(input))

    def test_5(self):
        input = 5
        self.assertEqual('V', self.obj.answer(input))

    def test_6(self):
        input = 6
        self.assertEqual('VI', self.obj.answer(input))

    def test_7(self):
        input = 7
        self.assertEqual('VII', self.obj.answer(input))

    def test_8(self):
        input = 8
        self.assertEqual('VIII', self.obj.answer(input))

    def test_9(self):
        input = 9
        self.assertEqual('IX', self.obj.answer(input))

    def test_10(self):
        input = 10
        self.assertEqual('X', self.obj.answer(input))

    def test_11(self):
        input = 11
        self.assertEqual('XI', self.obj.answer(input))

    def test_14(self):
        input = 14
        self.assertEqual('XIV', self.obj.answer(input))

    def test_15(self):
        input = 15
        self.assertEqual('XV', self.obj.answer(input))

    def test_21(self):
        input = 21
        self.assertEqual('XXI', self.obj.answer(input))

    def test_40(self):
        input = 40
        self.assertEqual('XL', self.obj.answer(input))

    def test_41(self):
        input = 41
        self.assertEqual('XLI', self.obj.answer(input))

    def test_42(self):
        input = 42
        self.assertEqual('XLII', self.obj.answer(input))

    def test_50(self):
        input = 50
        self.assertEqual('L', self.obj.answer(input))

    def test_51(self):
        input = 51
        self.assertEqual('LI', self.obj.answer(input))

    def test_89(self):
        input = 89
        self.assertEqual('LXXXIX', self.obj.answer(input))

    def test_90(self):
        input = 90
        self.assertEqual('XC', self.obj.answer(input))

    def test_91(self):
        self.assertEqual('XCI', self.obj.answer(91))

    def test_100(self):
        self.assertEqual('C', self.obj.answer(100))

    def test_399(self):
        self.assertEqual('CCCXCIX', self.obj.answer(399))

    def test_400(self):
        self.assertEqual('CD', self.obj.answer(400))

    def test_500(self):
        self.assertEqual('D', self.obj.answer(500))

    def test_899(self):
        self.assertEqual('DCCCXCIX', self.obj.answer(899))


    def test_900(self):
        self.assertEqual('CM', self.obj.answer(900))

    def test_1998(self):
        self.assertEqual('MCMXCVIII', self.obj.answer(1998))


if __name__ == '__main__':
    unittest.main()

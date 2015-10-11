import unittest
from solution import *


class TestWesternSigns(unittest.TestCase):
    def test_taurus_signs(self):
        self.assertEqual(interpret_western_sign(1, 5), 'taurus')

    def test_capricorn(self):
        self.assertEqual(interpret_western_sign(23, 12), 'capricorn')

    def test_gemini(self):
        self.assertEqual(interpret_western_sign(18, 6), 'gemini')

    def test_cancer(self):
        self.assertEqual(interpret_western_sign(19, 7), 'cancer')


class TestChineseSigns(unittest.TestCase):

    def test_tiger_sign(self):
        self.assertEqual(interpret_chinese_sign(1986), 'tiger')

    def test_dragon_sign(self):
        self.assertEqual(interpret_chinese_sign(2000), 'dragon')

    def test_dog_sign(self):
        self.assertEqual(interpret_chinese_sign(1994), 'dog')

    def test_monkey_sign(self):
        self.assertEqual(interpret_chinese_sign(1992), 'monkey')


class TestBothSigns(unittest.TestCase):
    def test_aries_snake_signs(self):
        self.assertEqual(
            interpret_both_signs(18, 4, 1989),
            ('aries', 'snake')
        )

    def test_aquarius_pig(self):
        self.assertEqual(
            interpret_both_signs(23, 1, 2007),
            ('aquarius', 'pig')
        )

    def test_leo_rat(self):
        self.assertEqual(
            interpret_both_signs(26, 7, 1936),
            ('leo', 'rat')
        )


if __name__ == '__main__':
    unittest.main()

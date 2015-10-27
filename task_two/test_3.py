import unittest

import solution as s


class ExtractTypeTest(unittest.TestCase):

    def test_aalabbalaa(self):
        input_ = [('a', 2), ('l', 1), ('error', 0), ('a', 1), ('b', 2),
                  ('a', 1), ('l', 1), ('a', 2)]
        self.assertEqual("aalabbalaa", s.extract_type(input_, str))

    def test_int(self):
        input_ = [({'a': 10}, 1), (1, 4), (0.2, 3), (2, 3), (True, 2),
                  (3, 2), ("something", 1), (4, 1), (5, 0)]
        self.assertEqual("1111222334", s.extract_type(input_, int))

    def test_bool(self):
        input_ = [(True, 1), ("and", 1), (False, 1), ('==', 1), (False, 1)]
        self.assertEqual("TrueFalseFalse", s.extract_type(input_, bool))

    def test_list_simitli(self):
        input_ = [(['S', 'I', 'M'], 1), (type, 2), (['I'], 1), ({}, 10),
                  (['T', 'L', 'I'], 1), ([1, 2, 3, 4], 0), (13, 1)]
        self.assertEqual("['S', 'I', 'M']['I']['T', 'L', 'I']",
                         s.extract_type(input_, list))

    def test_gopher(self):
        input_ = [('g', 1), ((1, 2), 3), ('op', 1), (3.1415, 1),
                  ('h', 1), (False, 1), ('e', 1), ([], 5), ('r', 1)]
        self.assertEqual("gopher", s.extract_type(input_, str))


class ReversedDictTest(unittest.TestCase):

    def test_animals(self):
        input_ = {"cat": 2, "dog": 1, "monkey": 1, "gopher": 3}
        output = s.reversed_dict(input_)
        self.assertEqual(output[2], "cat")
        self.assertEqual(output[3], "gopher")
        self.assertIn(1, output)

    def test_fruits_menu(self):
        input_ = {('apple', 'orange'): 'first', ('apple', 'cherry'): 'second',
                  ('cherry', 'orange'): 'third'}
        output = {'first': ('apple', 'orange'), 'second': ('apple', 'cherry'),
                  'third': ('cherry', 'orange')}
        self.assertEqual(s.reversed_dict(input_), output)


class FlattenDictTest(unittest.TestCase):

    def test_fruits_three_levels(self):
        input_ = {'pineapple': 1,
                  'apple': {'orange': 2,
                            'cherry': 2,
                            'peach': {'apricot': 1,
                                      'lemon': 1}},
                  'kiwi': 3}

        output = {'pineapple': 1, 'apple.orange': 2, 'apple.cherry': 2,
                  'apple.peach.apricot': 1, 'apple.peach.lemon': 1,
                  'kiwi': 3}
        self.assertEqual(s.flatten_dict(input_), output)

    def test_automobile_manufacturers(self):
        input_ = {'Sweden': 'Volvo',
                  'Germany': {'Wolfsburg': 'VW',
                              'Munich': 'BMW',
                              'Stuttgart': {'east': 'Porsche',
                                            'west': 'Mercedes'}},
                  'Chemnitz': 'Audi'}

        output = {'Sweden': 'Volvo', 'Germany.Wolfsburg': 'VW',
                  'Germany.Munich': 'BMW',
                  'Germany.Stuttgart.east': 'Porsche',
                  'Germany.Stuttgart.west': 'Mercedes', 'Chemnitz': 'Audi'}
        self.assertEqual(s.flatten_dict(input_), output)


class UnflattenDictTest(unittest.TestCase):

    def test_fruits_three_levels(self):
        input_ = {'pineapple': 1, 'apple.orange': 2, 'apple.cherry': 2,
                  'apple.peach.apricot': 1, 'apple.peach.lemon': 1,
                  'kiwi': 3}

        output = {'pineapple': 1,
                  'apple': {'orange': 2,
                            'cherry': 2,
                            'peach': {'apricot': 1,
                                      'lemon': 1}},
                  'kiwi': 3}
        self.assertEqual(s.unflatten_dict(input_), output)

    def test_automobile_manufacturers(self):
        input_ = {'Sweden': 'Volvo', 'Germany.Wolfsburg': 'VW',
                  'Germany.Munich': 'BMW',
                  'Germany.Stuttgart.east': 'Porsche',
                  'Germany.Stuttgart.west': 'Mercedes', 'Chemnitz': 'Audi'}

        output = {'Sweden': 'Volvo',
                  'Germany': {'Wolfsburg': 'VW',
                              'Munich': 'BMW',
                              'Stuttgart': {'east': 'Porsche',
                                            'west': 'Mercedes'}},
                  'Chemnitz': 'Audi'}
        self.assertEqual(s.unflatten_dict(input_), output)


class RepsTest(unittest.TestCase):

    def test_empty(self):
        input_ = [1, 2, 3, 4, 5]
        self.assertEqual(s.reps(input_), ())

    def test_with_letters(self):
        input_ = ['s', 'i', 'm', 'i', 't', 'l', 'i',
                  's', 'i', 'm', 'i', 't', 'l', 'i', 'x', 'y', 'z']
        output = ('s', 'i', 'm', 'i', 't', 'l', 'i',
                  's', 'i', 'm', 'i', 't', 'l', 'i')
        self.assertEqual(s.reps(input_), output)

    def test_with_bool(self):
        input_ = True, False, True, True
        output = True, True, True
        self.assertEqual(s.reps(input_), output)

    def test_with_int(self):
        input_ = 1, 2, 1, 3, 1, 4, 1, 5
        output = 1, 1, 1, 1
        self.assertEqual(s.reps(input_), output)

    def test_with_dict(self):
        input_ = {}, {'a': 1}, {}, {'a': 2}, {'a': 1}, {}
        output = {}, {'a': 1}, {}, {'a': 1}, {}
        self.assertEqual(s.reps(input_), output)


if __name__ == '__main__':
    unittest.main()

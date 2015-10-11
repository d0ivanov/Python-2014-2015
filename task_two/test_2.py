import unittest
import solution


class ExtractTypeTest(unittest.TestCase):
    def test_python(self):
        input = [('p', 1), ('y', 1), ('t', 1),
                 ('h', 1), ('o', 1), ('n', 1)]
        self.assertEqual("python", solution.extract_type(input, str))

    def test_some_types(self):
        input = [('a', 1), (5, 10), ('p', 2),
                 ('l', 1), ('e', 1), (14, 2)]
        self.assertEqual("apple", solution.extract_type(input, str))

    def test_fave(self):
        input = [('r', 1), ('o', 1), (1, 1), ('s', 2), ('o', 1), (5, 0),
                 ('n', 1), ('e', 1), (1, 2), ('r', 1), ('o', 1)]
        self.assertEqual("rossonero", solution.extract_type(input, str))
        
    def test_bg(self):
        input = [('B', 1), ('u', 1), (1, 1), ('l', 1), ('g', 1),
                 ('a', 1), ('r', 1), ('i', 1), (1, 2), (4, 3),
                 ('a', 1), (3, 1)]
        self.assertEqual("Bulgaria", solution.extract_type(input, str))


    def test_num(self):
        input = [('B', 1), ('u', 1), (1, 1), ('l', 1), ('g', 1),
                 ('a', 1), ('r', 1), ('i', 1), (1, 2), (4, 3),
                 ('a', 1), (3, 1)]
        self.assertEqual("1114443", solution.extract_type(input, int))


class ReversedDictTest(unittest.TestCase):
    def test_sports(self):
        input = {'Football': '1', 'Volleyball': '3',
                 'Basketball': '4', 'Tennis': '2', 'Soccer': 'wtf'}
        output = {'1': 'Football', '2': 'Tennis', '3': 'Volleyball',
                  '4': 'Basketball', 'wtf': 'Soccer'}
        self.assertEqual(solution.reversed_dict(input), output)
    
    def test_teams(self):
        input = {'Milan': 'Italy', 'Levski': 'Bulgaria',
                 'Borussia': 'Germany', 'Atletico': 'Spain',
                 'Arsenal': 'England', 'PSG': 'France'}
        output = {'Italy': 'Milan', 'Bulgaria': 'Levski',
                  'Germany': 'Borussia', 'Spain': 'Atletico',
                  'England': 'Arsenal', 'France': 'PSG'}
        self.assertEqual(solution.reversed_dict(input), output)


class FlattenDictTest(unittest.TestCase):
    def test_with_three_levels(self):
        self.assertEqual({'three.threeOne.threeOneOne': 3.11,
                          'two.twoOne': 2.1, 'one': 1},
                          solution.flatten_dict({'one': 1,
                          'two': {'twoOne': 2.1},
                          'three': {'threeOne': {'threeOneOne': 3.11}}}))


    def test_three_levels(self):
        self.assertEqual({'g': 103, 'a.b': 195, 'c.d.e.f': 402},
                          solution.flatten_dict({'a': {'b': 195},
                          'c': {'d': {'e': {'f': 402}}},
                          'g': 103}))


class UnflattenDictTest(unittest.TestCase):
    def test_with_three_levels(self):
        self.assertEqual({'g': 103, 'c': {'d': {'e': {'f': 402}}}, 'a': {'b': 195}},
                         solution.unflatten_dict({'g': 103, 'a.b': 195, 'c.d.e.f': 402}))

    def test_three(self):
        self.assertEqual({'one': 1, 'three': {'threeOne': {'threeOneOne': 3.11}},
                         'two': {'twoOne': 2.1}},
                         solution.unflatten_dict({'three.threeOne.threeOneOne': 3.11,
                         'two.twoOne': 2.1, 'one': 1}))

class RepsTest(unittest.TestCase):
    def test_full(self):
        self.assertEqual((1, 1, 1, 1), solution.reps((1, 1, 1, 1)))

    def test_empty(self):
        self.assertEqual((), solution.reps((1,2,3,4,5,6)))
    
    def test_fullone(self):
        self.assertEqual((1, 2, 3, 3, 2, 1),
                         solution.reps([1,2,3,3,2,1]))
    
    def test_empty_gain(self):
        self.assertEqual((), solution.reps([]))
    
    def test_some(self):
        self.assertEqual((4, 4, 4, 7, 7), solution.reps([4,5,4,1,4,7,76,54,3,7]))


if __name__ == '__main__':
    unittest.main()

import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def split_words(x):
    abba_allowed, abba_disallowed = [], []
    current_word = []
    in_disallowed = False

    for c in x:
        if c == '[':
            assert(in_disallowed == False)
            abba_allowed.append(''.join(current_word))
            current_word = []
            in_disallowed = True
            continue
        if c == ']':
            assert(in_disallowed == True)
            abba_disallowed.append(''.join(current_word))
            current_word = []
            in_disallowed = False
            continue
        current_word.append(c)
    if len(current_word) > 0:
        if in_disallowed:
            abba_disallowed.append(''.join(current_word))
        else:
            abba_allowed.append(''.join(current_word))
    return abba_allowed, abba_disallowed


def has_abba(word):
    for i in range(len(word) - 3):
        a = word[i]
        b = word[i + 1]
        c = word[i + 2]
        d = word[i + 3]
        if a == b:
            continue
        if a == d and b == c:
            return True
    return False



def is_valid(abba_allowed, abba_disallowed):
    abba_count = 0
    for x in abba_allowed:
        if has_abba(x):
            abba_count +=1
    if abba_count == 0:
        return False
    for x in abba_disallowed:
        if has_abba(x):
            return False
    return True



def part_one(filename):
    data = read_puzzle_input(filename)
    for x in data:
        abba_allowed, abba_disallowed = split_words(x)
        if is_valid(abba_allowed, abba_disallowed):
            pass


part_one('Day_07_short_input.txt')

class Test(unittest.TestCase):
    def test_split_words(self):
        abba_allowed, abba_disallowed = split_words('ioxxoj[asdfgh]zxcvbn')
        self.assertEqual(2, len(abba_allowed))
        self.assertEqual(1, len(abba_disallowed))
        self.assertEqual('ioxxoj', abba_allowed[0])
        self.assertEqual('zxcvbn', abba_allowed[1])
        self.assertEqual('asdfgh', abba_disallowed[0])

    def test_has_abba(self):
        self.assertTrue(has_abba('ioxxoj'))
        self.assertTrue(has_abba('abba'))
        self.assertFalse(has_abba('asdfgh'))



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
            assert (in_disallowed == False)
            abba_allowed.append(''.join(current_word))
            current_word = []
            in_disallowed = True
            continue
        if c == ']':
            assert (in_disallowed == True)
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


def find_abas(word):
    abas = []
    for i in range(len(word) - 2):
        a = word[i]
        b = word[i + 1]
        c = word[i + 2]
        if a == c and a != b:
            abas.append(a + b + c)
    return abas


def supports_tls(abba_allowed, abba_disallowed):
    abba_count = 0
    for x in abba_allowed:
        if has_abba(x):
            abba_count += 1
    if abba_count == 0:
        return False
    for x in abba_disallowed:
        if has_abba(x):
            return False
    return True


def supports_ssl(abba_allowed, abba_disallowed):
    abas_outside = []
    for x in abba_allowed:
        abas_outside.extend(find_abas(x))
    abas_inside = []
    for x in abba_disallowed:
        abas_inside.extend(find_abas(x))
    for x in abas_outside:
        a = x[0]
        b = x[1]
        bab = b + a + b
        if bab in abas_inside:
            return True
    return False


def part_one(filename):
    data = read_puzzle_input(filename)
    valid_tally = 0
    for x in data:
        abba_allowed, abba_disallowed = split_words(x)
        if supports_tls(abba_allowed, abba_disallowed):
            valid_tally += 1
    return valid_tally


def part_two(filename):
    data = read_puzzle_input(filename)
    valid_tally = 0
    for x in data:
        abba_allowed, abba_disallowed = split_words(x)
        if supports_ssl(abba_allowed, abba_disallowed):
            valid_tally += 1
    return valid_tally


print('Supports SSL:', part_two('Day_07_input.txt'))


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

    def test_part_one(self):
        self.assertEqual(110, part_one('Day_07_input.txt'))
        self.assertEqual(2, part_one('Day_07_short_input.txt'))

    def test_part_two(self):
        self.assertEqual(3, part_two('Day_07_short_input_02.txt'))
        self.assertEqual(242, part_two('Day_07_input.txt'))

import math
import unittest


def load_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def tally_chars(data, index):
    char_tallies = {}
    for x in data:
        c = x[index]
        if c in char_tallies.keys():
            char_tallies[c] += 1
        else:
            char_tallies[c] = 1
    return char_tallies


def pick_most_common(char_tallies: dict):
    max_value = 0
    max_letter = None
    for k, v in char_tallies.items():
        if v > max_value:
            max_value = v
            max_letter = k

    return max_letter


def pick_least_common(char_tallies):
    min_value = math.inf
    min_letter = None
    for k, v in char_tallies.items():
        if v < min_value:
            min_value = v
            min_letter = k

    return min_letter


def part_one(filename):
    data = load_puzzle_input(filename)
    width = len(data[0])
    decrypted_message = []
    for i in range(width):
        char_tallies = tally_chars(data, i)
        c = pick_most_common(char_tallies)
        decrypted_message.append(c)
    return ''.join(decrypted_message)


def part_two(filename):
    data = load_puzzle_input(filename)
    width = len(data[0])
    decrypted_message = []
    for i in range(width):
        char_tallies = tally_chars(data, i)
        c = pick_least_common(char_tallies)
        decrypted_message.append(c)
    return ''.join(decrypted_message)


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual('easter', part_one('Day_06_short_input.txt'))
        self.assertEqual('xhnqpqql', part_one('Day_06_input.txt'))

    def test_part_two(self):
        self.assertEqual('advent', part_two('Day_06_short_input.txt'))
        self.assertEqual('brhailro', part_two('Day_06_input.txt'))

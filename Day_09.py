import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        compressed_file = f.read().strip()
    return compressed_file


def handle_marker(marker, i, compressed_file):
    result = re.search('\((\d+)x(\d+)\)', marker)
    number_of_chars = result.group(1)
    repetitions = result.group(2)

def decompress_file(compressed_file):
    rval = []
    marker = []
    in_marker = False
    for i, c in enumerate(compressed_file):
        if c == '(':
            in_marker = True
        if in_marker:
            marker.append(c)
            if c == ')':
                in_marker = False
                handle_marker(''.join(marker), i, compressed_file)
        else:
            rval.append(c)
    return ''.join(rval)


def part_one(filename):
    compressed_file = read_puzzle_input(filename)
    # decompressed_file = decompress_file(compressed_file)

print(part_one('Day_09_input.txt'))

class Test(unittest.TestCase):
    def test_decompress_file(self):
        self.assertEqual('ADVENT', decompress_file('ADVENT'))
        self.assertEqual('ABBBBBC', decompress_file('A(1x5)BC'))
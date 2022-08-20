import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        compressed_file = f.read().strip()
    return [c for c in compressed_file]


def handle_marker(marker, i, compressed_file, decompressed_file):
    result = re.search('\((\d+)x(\d+)\)', marker)
    number_of_chars = int(result.group(1))
    repetitions = int(result.group(2))
    i += 1
    for _ in range(repetitions):
        for j in range(i, i + number_of_chars):
            if j >= len(compressed_file):
                continue
            decompressed_file.append(compressed_file[j])
    return number_of_chars


def decompress_file(compressed_file):
    decompressed_file = []
    marker = []
    in_marker = False
    skip = 0
    for i, c in enumerate(compressed_file):
        if skip:
            skip -= 1
            continue
        if c == '(':
            in_marker = True
        if in_marker:
            marker.append(c)
            if c == ')':
                in_marker = False
                skip = handle_marker(''.join(marker), i, compressed_file, decompressed_file)
        else:
            decompressed_file.append(c)
    return ''.join(decompressed_file)


def part_one(filename):
    compressed_file = read_puzzle_input(filename)
    decompressed_file = decompress_file(compressed_file).strip()
    print('Decompressed length', len(decompressed_file))
    print(decompressed_file)


print(part_one('Day_09_input.txt'))

# 87293 is too high
class Test(unittest.TestCase):
    def test_decompress_file(self):
        self.assertEqual('ADVENT', decompress_file('ADVENT'))
        self.assertEqual('ABBBBBC', decompress_file('A(1x5)BC'))
        self.assertEqual('XYZXYZXYZ', decompress_file('(3x3)XYZ'))
        self.assertEqual('ABCBCDEFEFG', decompress_file('A(2x2)BCD(2x2)EFG'))
        self.assertEqual('(1x3)A', decompress_file('(6x1)(1x3)A'))



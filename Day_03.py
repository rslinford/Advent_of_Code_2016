import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data =[x.strip().split() for x in f.read().strip().split('\n')]
    return data

def part_one(filename):
    triangles = read_puzzle_input(filename)
    possible_triangle_tally = 0
    for a, b, c in triangles:
        a = int(a)
        b = int(b)
        c = int(c)
        if a + b <= c:
            continue
        if b + c <= a:
            continue
        if c + a <= b:
            continue
        possible_triangle_tally += 1
    return possible_triangle_tally

def part_one(filename):
    triangles = read_puzzle_input(filename)
    possible_triangle_tally = 0
    return possible_triangle_tally

print('Possible triangles', part_two('Day_03_input.txt'))

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(1, part_one('Day_03_short_input.txt'))
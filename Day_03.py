import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data =[x.strip().split() for x in f.read().strip().split('\n')]
    return data

def is_possible_triange(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


def part_one(filename):
    triangles = read_puzzle_input(filename)
    possible_triangle_tally = 0
    for a, b, c in triangles:
        if is_possible_triange(a, b, c):
            possible_triangle_tally += 1
    return possible_triangle_tally

# It's not 646
def part_two(filename):
    triangles = read_puzzle_input(filename)
    possible_triangle_tally = 0
    for i in range(0, len(triangles), 3):
        if is_possible_triange(triangles[i][0], triangles[i+1][0], triangles[i + 2][0]):
            possible_triangle_tally += 1
        if is_possible_triange(triangles[i][1], triangles[i + 1][1], triangles[i + 2][1]):
            possible_triangle_tally += 1
        if is_possible_triange(triangles[i][2], triangles[i + 1][2], triangles[i + 2][2]):
            possible_triangle_tally += 1
    return possible_triangle_tally

print('Possible triangles', part_two('Day_03_input.txt'))

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(1, part_one('Day_03_short_input.txt'))
        self.assertEqual(1050, part_one('Day_03_input.txt'))

    def test_part_two(self):
        self.assertEqual(1921, part_two('Day_03_input.txt'))
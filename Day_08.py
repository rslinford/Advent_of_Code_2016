import numpy as np

class Screen:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.grid = np.empty((height, width), dtype=str)
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = '.'
    def __repr__(self):
        return str(self.grid)

def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def part_one(filename):
    data = read_puzzle_input(filename)
    screen = Screen(3, 7)
    print(screen)

part_one('Day_08_short_input.txt')

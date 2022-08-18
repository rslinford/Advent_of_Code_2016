import re
import unittest

import numpy as np

class Screen:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = np.empty((height, width), dtype=str)
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = '.'
    def __repr__(self):
        return str(self.grid)
    def draw_rectangle(self, height, width):
        for y in range(height):
            for x in range(width):
                self.grid[y][x] = '#'

    def rotate_column(self, col, amount):
        shift_size = amount % self.height
        for _ in range(shift_size):
            hold = self.grid[self.height-1][col]
            for y in range(self.height-1, 0, -1):
                self.grid[y][col] = self.grid[y-1][col]
            self.grid[0][col] = hold


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data

def handle_rect_command(command, screen):
    result = re.search('^rect (\d+)x(\d+)$', command)
    height = int(result.group(2))
    width = int(result.group(1))
    screen.draw_rectangle(height, width)


def handle_rotate_command(command, screen):
    result = re.search('^rotate \w+ (\w)=(\d+) by (\d+)', command)
    x_or_y = result.group(1)
    x_or_y_value = int(result.group(2))
    amount = int(result.group(3))
    if x_or_y == 'x':
        screen.rotate_column(x_or_y_value, amount)


def part_one(filename):
    data = read_puzzle_input(filename)
    screen = Screen(3, 7)
    for command in data:
        if command.find('rect') == 0:
            handle_rect_command(command, screen)
        elif command.find('rotate') == 0:
            handle_rotate_command(command, screen)
        else:
            raise ValueError(f'Expected "rect" or "rotate" found{command}')

part_one('Day_08_short_input.txt')

class Test(unittest.TestCase):
    def test_rotate_column(self):
        screen = Screen(4, 4)
        screen.grid[0][2] = '#'
        screen.grid[2][2] = '#'
        self.assertEqual("[['.' '.' '#' '.']\n"
                         " ['.' '.' '.' '.']\n"
                         " ['.' '.' '#' '.']\n"
                         " ['.' '.' '.' '.']]", str(screen))
        screen.rotate_column(2, 1)
        self.assertEqual("[['.' '.' '.' '.']\n"
                         " ['.' '.' '#' '.']\n"
                         " ['.' '.' '.' '.']\n"
                         " ['.' '.' '#' '.']]", str(screen))
        screen.rotate_column(2, 1)
        self.assertEqual("[['.' '.' '#' '.']\n"
                         " ['.' '.' '.' '.']\n"
                         " ['.' '.' '#' '.']\n"
                         " ['.' '.' '.' '.']]", str(screen))
        screen.rotate_column(2, 2)
        self.assertEqual("[['.' '.' '#' '.']\n"
                         " ['.' '.' '.' '.']\n"
                         " ['.' '.' '#' '.']\n"
                         " ['.' '.' '.' '.']]", str(screen))
        screen.grid[0][0] = '#'
        self.assertEqual("[['#' '.' '#' '.']\n"
                         " ['.' '.' '.' '.']\n"
                         " ['.' '.' '#' '.']\n"
                         " ['.' '.' '.' '.']]", str(screen))
        screen.rotate_column(0, 3)
        self.assertEqual("[['.' '.' '#' '.']\n"
                         " ['.' '.' '.' '.']\n"
                         " ['.' '.' '#' '.']\n"
                         " ['#' '.' '.' '.']]", str(screen))

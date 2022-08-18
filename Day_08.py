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

    def rotate_row(self, row, amount):
        shift_size = amount % self.width
        for _ in range(shift_size):
            hold = self.grid[row][self.width-1]
            for x in range(self.width - 1, 0, -1):
                self.grid[row][x] = self.grid[row][x - 1]
            self.grid[row][0] = hold

    def count_lit_pixils(self):
        tally = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == '#':
                    tally += 1
        return tally


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
    elif x_or_y == 'y':
        screen.rotate_row(x_or_y_value, amount)
    else:
        raise ValueError(f'Expected "x" or "y" found "{x_or_y}"')

def handle_command(command, screen):
    if command.find('rect') == 0:
        handle_rect_command(command, screen)
    elif command.find('rotate') == 0:
        handle_rotate_command(command, screen)
    else:
        raise ValueError(f'Expected "rect" or "rotate" found "{command}"')


def part_one(filename):
    commands = read_puzzle_input(filename)
    screen = Screen(6, 50)
    for command in commands:
        handle_command(command, screen)
    return screen.count_lit_pixils()


def part_two(filename):
    commands = read_puzzle_input(filename)
    screen = Screen(6, 50)
    for command in commands:
        handle_command(command, screen)
    print(screen)
    return screen.count_lit_pixils()


print('Lit pixel count:', part_two('Day_08_input.txt'))

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(121, part_one('Day_08_input.txt'))

    def test_short_data(self):
        commands = read_puzzle_input('Day_08_short_input.txt')
        screen = Screen(3, 7)
        self.assertEqual("[['.' '.' '.' '.' '.' '.' '.']\n"
                         " ['.' '.' '.' '.' '.' '.' '.']\n"
                         " ['.' '.' '.' '.' '.' '.' '.']]", str(screen))
        index = 0
        handle_command(commands[0], screen)
        self.assertEqual("[['#' '#' '#' '.' '.' '.' '.']\n"
                         " ['#' '#' '#' '.' '.' '.' '.']\n"
                         " ['.' '.' '.' '.' '.' '.' '.']]", str(screen))
        handle_command(commands[1], screen)
        self.assertEqual("[['#' '.' '#' '.' '.' '.' '.']\n"
                         " ['#' '#' '#' '.' '.' '.' '.']\n"
                         " ['.' '#' '.' '.' '.' '.' '.']]", str(screen))
        handle_command(commands[2], screen)
        self.assertEqual("[['.' '.' '.' '.' '#' '.' '#']\n"
                         " ['#' '#' '#' '.' '.' '.' '.']\n"
                         " ['.' '#' '.' '.' '.' '.' '.']]", str(screen))
        handle_command(commands[3], screen)
        self.assertEqual("[['.' '#' '.' '.' '#' '.' '#']\n"
                         " ['#' '.' '#' '.' '.' '.' '.']\n"
                         " ['.' '#' '.' '.' '.' '.' '.']]", str(screen))
        self.assertEqual(6, screen.count_lit_pixils())


    def test_rotate_row(self):
        screen = Screen(3, 4)
        screen.grid[1][0] = '#'
        screen.grid[1][3] = '#'
        self.assertEqual("[['.' '.' '.' '.']\n"
                         " ['#' '.' '.' '#']\n"
                         " ['.' '.' '.' '.']]", str(screen))
        screen.rotate_row(1, 1)
        self.assertEqual("[['.' '.' '.' '.']\n"
                         " ['#' '#' '.' '.']\n"
                         " ['.' '.' '.' '.']]", str(screen))
        screen.rotate_row(1, 2)
        self.assertEqual("[['.' '.' '.' '.']\n"
                         " ['.' '.' '#' '#']\n"
                         " ['.' '.' '.' '.']]", str(screen))


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

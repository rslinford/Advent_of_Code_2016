import unittest
from enum import Enum


class Button(Enum):
    NONE = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    A = 10
    B = 11
    C = 12
    D = 13


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


"""
1 2 3
4 5 6
7 8 9
"""


class StandardKeypad:
    def __init__(self):
        self.button_map = {Button.ONE: [Button.NONE, Button.TWO, Button.FOUR, Button.NONE],
                           Button.TWO: [Button.NONE, Button.THREE, Button.FIVE, Button.ONE],
                           Button.THREE: [Button.NONE, Button.NONE, Button.SIX, Button.TWO],
                           Button.FOUR: [Button.ONE, Button.FIVE, Button.SEVEN, Button.NONE],
                           Button.FIVE: [Button.TWO, Button.SIX, Button.EIGHT, Button.FOUR],
                           Button.SIX: [Button.THREE, Button.NONE, Button.NINE, Button.FIVE],
                           Button.SEVEN: [Button.FOUR, Button.EIGHT, Button.NONE, Button.NONE],
                           Button.EIGHT: [Button.FIVE, Button.NINE, Button.NONE, Button.SEVEN],
                           Button.NINE: [Button.SIX, Button.NONE, Button.NONE, Button.EIGHT]}
        self.current_button = Button.FIVE

    def __repr__(self):
        return f'{self.__class__.__name__}  current_button:{self.current_button}'

    def move(self, direction):
        urdl = self.button_map.get(self.current_button)
        if urdl[direction.value] != Button.NONE:
            self.current_button = urdl[direction.value]
            return True
        else:
            return False


"""
    1
  2 3 4
5 6 7 8 9
  A B C
    D
"""


class ElfKeypad(StandardKeypad):
    def __init__(self):
        self.button_map = {Button.ONE: [Button.NONE, Button.NONE, Button.THREE, Button.NONE],
                           Button.TWO: [Button.NONE, Button.THREE, Button.SIX, Button.NONE],
                           Button.THREE: [Button.ONE, Button.FOUR, Button.SEVEN, Button.TWO],
                           Button.FOUR: [Button.NONE, Button.NONE, Button.EIGHT, Button.THREE],
                           Button.FIVE: [Button.NONE, Button.SIX, Button.NONE, Button.NONE],
                           Button.SIX: [Button.TWO, Button.SEVEN, Button.A, Button.FIVE],
                           Button.SEVEN: [Button.THREE, Button.EIGHT, Button.B, Button.SIX],
                           Button.EIGHT: [Button.FOUR, Button.NINE, Button.C, Button.SEVEN],
                           Button.NINE: [Button.NONE, Button.NONE, Button.NONE, Button.EIGHT],
                           Button.A: [Button.SIX, Button.B, Button.NONE, Button.NONE],
                           Button.B: [Button.SEVEN, Button.C, Button.D, Button.A],
                           Button.C: [Button.EIGHT, Button.NONE, Button.NONE, Button.B],
                           Button.D: [Button.B, Button.NONE, Button.NONE, Button.NONE]}
        self.current_button = Button.FIVE


def load_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data


def code_hunt(rows, keypad):
    code = []
    for row in rows:
        for c in row:
            match c:
                case 'U':
                    keypad.move(Direction.UP)
                case 'R':
                    keypad.move(Direction.RIGHT)
                case 'D':
                    keypad.move(Direction.DOWN)
                case 'L':
                    keypad.move(Direction.LEFT)
        if keypad.current_button.value <= 9:
            code.append(str(keypad.current_button.value))
        else:
            code.append(str(keypad.current_button.name))
    return "".join(code)


def part_one(filename):
    data = load_puzzle_input(filename)
    keypad = StandardKeypad()
    return code_hunt(data, keypad)


def part_two(filename):
    data = load_puzzle_input(filename)
    keypad = ElfKeypad()
    return code_hunt(data, keypad)


print('Code', part_two('Day_02_input.txt'))


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual('1985', part_one('Day_02_short_input.txt'))
        self.assertEqual('97289', part_one('Day_02_input.txt'))

    def test_part_two(self):
        self.assertEqual('5DB3', part_two('Day_02_short_input.txt'))
        self.assertEqual('9A7DC', part_two('Day_02_input.txt'))

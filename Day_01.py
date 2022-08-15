import unittest
from enum import Enum


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


class Turtle:
    def __init__(self):
        self.x, self.y = 0, 0
        self.direction = Direction.NORTH
        self.been_there = set()
        self.been_there.add((0, 0))

    def distance_from_origin(self):
        return abs(self.x) + abs(self.y)

    def walk_forward(self, distance):
        for _ in range(distance):
            match self.direction:
                case Direction.NORTH:
                    self.y += 1
                case Direction.EAST:
                    self.x += 1
                case Direction.SOUTH:
                    self.y -= 1
                case Direction.WEST:
                    self.x -= 1
            t = (self.x, self.y)
            if t in self.been_there:
                print(f'Been here {t} already. Distance {self.distance_from_origin()}')
            self.been_there.add(t)

    def rotate_left_and_walk_forward(self, distance):
        match self.direction:
            case Direction.NORTH:
                self.direction = Direction.WEST
            case Direction.EAST:
                self.direction = Direction.NORTH
            case Direction.SOUTH:
                self.direction = Direction.EAST
            case Direction.WEST:
                self.direction = Direction.SOUTH
        self.walk_forward(distance)

    def rotate_right_and_walk_forward(self, distance):
        match self.direction:
            case Direction.NORTH:
                self.direction = Direction.EAST
            case Direction.EAST:
                self.direction = Direction.SOUTH
            case Direction.SOUTH:
                self.direction = Direction.WEST
            case Direction.WEST:
                self.direction = Direction.NORTH
        self.walk_forward(distance)


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split(', ')
    return data


def part_one(filename):
    data = read_puzzle_input(filename)
    turtle = Turtle()
    for d in data:
        rotation = d[0]
        distance = int(d[1:])
        if rotation == 'L':
            turtle.rotate_left_and_walk_forward(distance)
        elif rotation == 'R':
            turtle.rotate_right_and_walk_forward(distance)
    return turtle.distance_from_origin()

def part_two(filename):
    data = read_puzzle_input(filename)
    turtle = Turtle()
    for d in data:
        rotation = d[0]
        distance = int(d[1:])
        if rotation == 'L':
            turtle.rotate_left_and_walk_forward(distance)
        elif rotation == 'R':
            turtle.rotate_right_and_walk_forward(distance)
    return turtle.distance_from_origin()

part_two('Day_01_input.txt')

class TestTurtle(unittest.TestCase):
    pass
    # def test_part_one(self):
    #     self.assertEqual(243, part_one('Day_01_input.txt'))
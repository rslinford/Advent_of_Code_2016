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

    def distance_from_origin(self):
        return self.x + self.y

    def walk_forward(self, distance):
        match self.direction:
            case Direction.NORTH:
                self.y += distance
            case Direction.EAST:
                self.x += distance
            case Direction.SOUTH:
                self.y -= distance
            case Direction.WEST:
                self.x -= distance

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
    print(f'Distance from origin {turtle.distance_from_origin()}')


part_one('Day_01_input.txt')

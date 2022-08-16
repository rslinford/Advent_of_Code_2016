def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data

def part_one(filename):
    data = read_puzzle_input(filename)
    print(data)


part_one('Day_04_short_input.txt')
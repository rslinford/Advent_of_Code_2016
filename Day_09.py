def part_one(filename):
    with open(filename, 'r') as f:
        compressed_file = f.read()
    return compressed_file


print(part_one('Day_09_input.txt'))
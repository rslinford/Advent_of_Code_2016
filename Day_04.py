import re
import unittest


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
    return data

def count_letters(letters):
    n = [c for c in letters]
    n.sort()
    letter_counts = {}
    for c in n:
        if c == '-':
            continue
        if c in letter_counts.keys():
            letter_counts[c] += 1
        else:
            letter_counts[c] = 1
    return letter_counts

def sort_key(e):
    return e[0]

def sort_by_value(letter_counts):
    flipped = []
    for k,v in letter_counts.items():
        flipped.append((v, k))
    flipped.sort(key=sort_key, reverse=True)
    return flipped


def top_five(letter_counts):
    word = []
    for x in letter_counts[0:5]:
        word.append(x[1])
    return ''.join(word)

def part_one(filename):
    rooms = read_puzzle_input(filename)
    sector_id_sum = 0
    for room in rooms:
        result = re.search(r'^([^\d]+)(\d+)\[(\w+)\]', room)
        name = result.group(1)
        sector_id = int(result.group(2))
        checksum = result.group(3)
        letter_counts = count_letters(name)
        letter_counts = sort_by_value(letter_counts)
        word = top_five(letter_counts)
        if word == checksum:
            sector_id_sum += sector_id
    return sector_id_sum


def shift_letter(letter, sector_id):
    a = ord(letter)
    for i in range(sector_id):
        a += 1
        if a > ord('z'):
            a = ord('a')
    return chr(a)



def decrypt_name(name, sector_id):
    decrypted = []
    for c in name:
        if c == '-':
            decrypted.append(' ')
        else:
            decrypted.append(shift_letter(c, sector_id))
    return ''.join(decrypted).strip()


def part_two(filename):
    rooms = read_puzzle_input(filename)
    for room in rooms:
        result = re.search(r'^([^\d]+)(\d+)\[(\w+)\]', room)
        name = result.group(1)
        sector_id = int(result.group(2))
        checksum = result.group(3)
        d_name = decrypt_name(name, sector_id)
        if d_name == 'northpole object storage':
            print(f'Decrypted name "{d_name}"  sector ID {sector_id}')
            return sector_id


print(part_two('Day_04_input.txt'))

class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(1514, part_one('Day_04_short_input.txt'))

    def test_part_two(self):
        self.assertEqual(482, part_two('Day_04_input.txt'))
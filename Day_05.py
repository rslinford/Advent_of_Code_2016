import hashlib
import unittest


def part_one(door_id):
    i = -1
    password = []
    while len(password) < 8:
        i += 1
        hash = hashlib.md5(door_id.encode('utf-8') + str(i).encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            password.append(hash[5])
            # print(door_id, i, hash)
    return ''.join(password)


def part_two(door_id):
    counter = -1
    password = ['-'] * 8
    while '-' in password:
        counter += 1
        hash = hashlib.md5(door_id.encode('utf-8') + str(counter).encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            # print('Before', door_id, counter, hash, password)
            index = int(hash[5], 16)
            c = hash[6]
            if index >= 8:
                continue  # ignore invalid positions
            if password[index] != '-':
                continue  # ignore positions that have been filled in already
            password[index] = c
            print(door_id, counter, hash, password)
    return ''.join(password)


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual('18f47a30', part_one('abc'))
        self.assertEqual('f77a0e6e', part_one('cxdnnyjw'))
        pass

    def test_part_two(self):
        self.assertEqual('05ace8e3', part_two('abc'))
        self.assertEqual('999828ec', part_two('cxdnnyjw'))

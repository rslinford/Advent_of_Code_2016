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
            print(door_id, i, hash)
    return ''.join(password)




class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual('18f47a30', part_one('abc'))
        self.assertEqual('?', part_one('cxdnnyjw'))
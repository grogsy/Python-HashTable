import unittest
from hashtable import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.t = HashTable()

    def test_setget(self):
        self.t['cat'] = 'meow'
        self.t['foo'] = 'bar'
        self.t[1] = 'a'
        self.t[1111] = 25
        self.t[0.5] = 3

        self.assertEqual(self.t['cat'], 'meow')
        self.assertEqual(self.t['foo'], 'bar')
        self.assertEqual(self.t[1], 'a')
        self.assertEqual(self.t[1111], 25)
        self.assertEqual(self.t[0.5], 3)

        d = {'cow': 'moo', 'bird': 'chirp', 100: 50}
        for k in d:
            self.t[k] = d[k]

        for k in d:
            self.assertEqual(d[k], self.t[k])

    def test_bool(self):
        self.assertFalse(bool(self.t))
        self.t['foo'] = 5
        self.assertTrue(bool(self.t))

    def test_get(self):
        self.assertEqual(self.t.get('cat'), None)
        self.t['foo'] = 'bar'
        self.assertEqual(self.t.get('foo'), 'bar')
        self.assertEqual(self.t.get('chicken', 'chirp'), 'chirp')

    def test_del(self):
        self.t['foo'] = 'bar'
        self.t['baz'] = 'baa'
        del self.t['foo']
        self.assertEqual(len(self.t), 1)
        self.assertFalse('foo' in self.t)

        self.t['cow'] = 'moo'
        self.t['fish'] = 'bubble'
        self.t[1] = 5
        self.t[2] = 3
        keys = self.t.keys()
        for k in keys:
            del self.t[k]
        self.assertEqual(len(self.t), 0)

        for k in keys:
            self.assertFalse(k in self.t)

    def test_generator(self):
        self.t['foo'] = 'bar'
        self.t['7'] = 'lucky'
        self.t[5] = 5 * 10

        for k, v in self.t.items():
            self.assertEqual((k, v), (k, self.t[k]))

    def test_contains(self):
        self.t['foo'] = 'bar'
        self.t[1] = 1
        for i in range(2, 5):
            self.t[i] = i * 5

        for k in self.t.keys():
            self.assertEqual(k in self.t, True)

        fake_keys = 'apple carrots bananas berries'.split()
        for k in fake_keys:
            self.assertEqual(k in self.t, False)


if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest
from requirements import *
import random

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test = []
        ranges = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1500]
        for i in ranges:
            arr = [random.randint(1, 4000) for _ in range(i)]
            print(f"Sorting {i}")
            self.assertEqual(tim_sort(arr), sorted(arr))

if __name__ == '__main__':
    unittest.main()

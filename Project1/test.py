import unittest
from requirements import *
import random

class MyTestCase(unittest.TestCase):
    def test_sorts(self):
        test = []
        ranges = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1500]
        for i in ranges:
            arr = [random.randint(1, 4000) for _ in range(i)]
            print(f"Sorting {i}")
            all_sorted = sorted(arr)
            self.assertEqual(tim_sort(arr), all_sorted)
            self.assertEqual(insertion_sort(arr), all_sorted)
            self.assertEqual(shell_sort1(arr), all_sorted)

    def test_equals(self):
        x = [9 for i in range(1000)]
        self.assertEqual(tim_sort(x), x)


if __name__ == '__main__':
    unittest.main()

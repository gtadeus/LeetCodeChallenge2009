import unittest
from typing import List


class Solution:
    MAX_VALUE = 1e9
    ret_set = set()
    min_ = 0
    max_ = 0

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        self.min_ = low
        self.max_ = high
        for i in range(9):
            self.addNumber(i)
        ret_val = sorted(filter(self.filter_function, self.ret_set))
        return ret_val

    def filter_function(self, value):
        return value if value <= self.max_ and value >= self.min_ else None

    def addNumber(self, nr):
        current_number = nr
        self.ret_set.add(current_number)
        abort = False
        while current_number < self.MAX_VALUE and not abort:
            # current_number = self.addNumber_rr(ret_val)
            val = str(nr)
            new_nr = int(val[-1]) + 1
            if new_nr <= 9:
                current_number = self.addNumber(int(str(val) + str(new_nr)))
                return current_number
            else:
                abort = True
        return current_number


class TestDay14(unittest.TestCase):

    S = Solution()
    test_inp = [
        [100, 300],
        [1000, 13000],
    ]
    test_result = [
        [123, 234],
        [1234, 2345, 3456, 4567, 5678, 6789, 12345],
    ]

    def test_solution(self):
        for i, val in enumerate(self.test_inp):
            self.S.dic = {}
            try:
                self.assertListEqual(self.test_result[i],
                                     self.S.sequentialDigits(val[0], val[1]))
            except AssertionError:
                print("test case nr. ", i+1, " failed")
                raise AssertionError


if __name__ == "__main__":
    unittest.main()

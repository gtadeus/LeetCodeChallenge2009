import unittest
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.len_y = len(grid)
        self.len_x = len(grid[0])
        for y, val1 in enumerate(grid):
            for x, val2 in enumerate(grid[y]):
                if grid[y][x] == 1:
                    self.start = x, y
                elif grid[y][x] == 2:
                    self.end = x, y
                elif grid[y][x] == -1:
                    self.forbidden.append((x, y))
                else:
                    self.target += 1
        #print(self.start, self.end, self.forbidden, self.target)
        #print(self.len_x, self.len_y)
        self.run(self.start, [self.start])
        #print(self.count)
        return self.count

    def __init__(self):
        self.list = []
        self.target = 0
        self.count = 0
        self.forbidden = []
        self.len_x = 0
        self.len_y = 0

    def run(self, pos, list_):
        #print("*** running from ", pos)

        dx = (1, 0)
        dy = (0, 1)
        dx_ = (-1, 0)
        dy_ = (0, -1)

        for delta in [dx, dy, dx_, dy_]:
            di, dj = delta
            x, y = pos
            x += di
            y += dj

            if 0 <= x <= self.len_x-1 and 0 <= y <= self.len_y-1:
                if (x, y) not in self.forbidden and (x, y) not in list_:
                    #print("next: ", (x, y))
                    if (x, y) == self.end:
                        #print(len(list_))
                        if len(list_) == self.target +1:
                            self.count += 1
                            break
                        else:
                            continue
                    else:
                        #self.list.append((x, y))
                        self.run((x, y), list_+[(x, y)])
                    

class TestDay(unittest.TestCase):

    S = Solution()
    test_inp = [
        [[1, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 2, -1]],
    ]
    test_result = [
        2,
    ]

    def test_solution(self):
        for i, val in enumerate(self.test_inp):
            self.S.dic = {}
            try:
                self.assertEqual(self.test_result[i],
                                 self.S.uniquePathsIII(val))
            except AssertionError:
                print("test case nr. ", i+1, " failed")
                raise AssertionError


if __name__ == "__main__":
    unittest.main()

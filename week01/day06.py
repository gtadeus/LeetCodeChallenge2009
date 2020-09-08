import unittest

A = [[1,1,0],
    [0,1,0],
    [0,1,0]]
B = [[0,0,0],
    [0,1,1],
    [0,0,1]]


class Solution:
    def largestOverlap(self, A, B):
        n = len(A)
        max_overlap = 0
        for (dx, dy) in [(1,1), (-1, 1), (1, -1), (-1, -1)]:
            for shiftx in range(n):
                for shifty in range(n):
                    count = 0
                    for x in range(n):
                        for y in range(n):
                            if A[x][y] == 1:
                                (nx, ny) = x+dx*shiftx, y+dy*shifty
                                if 0 <= nx < n and 0 <= ny <n and B[nx][ny] == 1:
                                        count += 1
                    
                    max_overlap = max(max_overlap, count)
        return max_overlap

class TestDay06(unittest.TestCase):
    S = Solution()
    A_res = [[0, 0, 0],
            [0, 1, 1],
            [0, 0, 1]]

    def test_overlap(self):
        self.assertEqual(3, self.S.largestOverlap(A,B))
        self.assertEqual(1, self.S.largestOverlap([[1]], [[1]]))
        self.assertEqual(1, self.S.largestOverlap([[1,0],[0,0]], [[0,1],[1,0]]))
        self.assertEqual(2, self.S.largestOverlap([[0,1],[1,1]], [[0,1],[1,0]]))
        self.assertEqual(26, self.S.largestOverlap([[1,1,0,1,0,1,0,0,0,0],[0,1,1,1,0,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0],[0,1,0,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0],[0,1,1,0,0,0,1,0,0,0],[0,1,0,1,1,0,0,1,0,1],[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,1,0],[1,0,0,1,1,1,0,0,1,0]],[[1,1,1,1,1,0,1,1,1,1],[1,1,1,1,0,1,1,1,0,0],[1,1,1,1,0,1,1,0,1,1],[1,0,1,1,0,0,1,0,1,1],[1,1,0,1,1,1,0,0,1,1],[1,1,1,1,1,0,0,1,0,1],[0,1,1,1,1,1,1,0,1,1],[0,1,1,1,0,1,1,1,1,1],[1,0,1,1,1,1,1,1,0,0],[1,1,1,1,1,1,1,1,1,0]]))


if __name__ == '__main__':
    unittest.main()
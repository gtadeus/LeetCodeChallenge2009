import unittest
     
A = [[1,1,0],
    [0,1,0],
    [0,1,0]]
B = [[0,0,0],
    [0,1,1],
    [0,0,1]]


class Solution:
    def largestOverlap(self, A, B):
        max_overlap = 0
        n = len(A)
        for i in range(-n, n):
            
            for j in range(-n, n):
                #if (i != 0 and j != 0):
                    #print("i: ", i, " j: ", j)
                M = self.translate(A, i, j)
                overlap = self.calcOverlap(M, B)
                #print("overlap: ", overlap)
                if overlap > max_overlap:
                    max_overlap = overlap
        #self.translate(A, left=-1, top=-1)

        return max_overlap
    def calcOverlap(self, A, B):
        n = len(A)
        sum_ = 0
        for i in range(n):
            for j in range(n):
                if (A[i][j] == 1 and B[i][j]==1):
                    sum_ += 1
        return sum_
    def translate(self, A, left=0, top=0):
        n = len(A)
        M = []
        
        for i in range(n):
            N =[]
            for j in range(n):
                val_j = j + left
                val_i = i + top
                #print("here: ", val_i, val_j)
                if  val_j < 0 or val_j >= n or val_i < 0 or val_i >= n:
                    val = 0
                else:
                    val = A[val_i][val_j]                
                N.append(val)
            M.append(N)
        
        return M
            



class TestDay06(unittest.TestCase):
    S = Solution()
    A_res = [[0, 0, 0],
            [0, 1, 1],
            [0, 0, 1]]
    def test_overlap(self):
        self.assertEqual(3, self.S.largestOverlap(A,B))
        self.assertEqual(1, self.S.largestOverlap([[1]], [[1]]))
    def test_calc_overlap(self):
        self.assertEqual(3, self.S.calcOverlap(B, self.A_res))
    def test_translate(self):
        self.assertEqual(self.A_res, self.S.translate(A, -1, -1))

if __name__ == '__main__':
    unittest.main()
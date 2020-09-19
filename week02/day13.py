import unittest
 
class Solution:
    def insert(self, intervals, newInterval):
        print(intervals, newInterval)
        right = []
        left = []
        ret = []


        for i in intervals:
            if i[1]<newInterval[0]:
                left.append(i)
            elif i[0]>newInterval[1]:
                right.append(i)
            else:
                newInterval[0] = min(i[0], newInterval[0])
                newInterval[1] = max(i[1], newInterval[1])

        #print(left, newInterval, right)
        ret = left + [newInterval] + right
        #print(ret)
        return ret

class TestDay13(unittest.TestCase):

    S = Solution()
    test_inp = [
        [[[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]],
        [[[1,3],[6,9]],[2,5]],
        [[],[5,7]],
        [[[1,5]], [2,7]],
        [[[1,5]], [6,8]],
        [[[1,3],[6,9]], [2,5]],
        [[[1,5]], [0,3]],
        [[[1,5]],[0,0]],
        [[[1,5]],[0,6]],
        [[[0,2],[3,3],[6,11]], [9,15]],
        [[[0,5],[9,12]], [7,16]],
        [[[0,7],[8,8],[9,11]], [4,13]]

    ]
    test_result = [
        [[1,2],[3,10],[12,16]],
         [[1,5],[6,9]],
         [[5,7]],
         [[1,7]],
         [[1,5],[6,8]],
     [[1,5],[6,9]],
        [[0,5]],
         [[0,0],[1,5]],
         [[0,6]],
         [[0,2],[3,3],[6,15]],
         [[0,5],[7,16]],
         [[0,13]]
    ]

    def test_solution(self):
        for i, val in enumerate(self.test_inp):
            
            try:
                self.assertCountEqual(self.test_result[i], self.S.insert(val[0], val[1]))
            except:
                print("test case nr. ", i+1, " failed")
                raise AssertionError
if __name__ == "__main__":
    unittest.main()

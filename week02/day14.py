import unittest
 
class Solution:
    dic = {}
    def rob(self, nums):
        if len(nums)<3:
            return max(nums)
        r = self.rr(nums, 0)
        print(self.dic)
        return r
    def rr(self, nums, start):
        results = []
        #if len(nums)<3:
        #    return max(nums)
        if start >= len(nums):
                return 0
        else:
            if start in self.dic.keys():
                return self.dic[start]
            else:
                m = 0
                rob = nums[start] + self.rr(nums, start+2)
                noRob = self.rr(nums, start+1)
                m = max(rob, noRob)
                self.dic[start] = m
                return m

class TestDay14(unittest.TestCase):

    S = Solution()
    test_inp = [
[1,2,3,1],
[2,7,9,3,1],
[2,1,1,2]

    ]
    test_result = [
4,
12,
4
    ]

    def test_solution(self):
        for i, val in enumerate(self.test_inp):
            self.S.dic={}
            try:
                self.assertEqual(self.test_result[i], self.S.rob(val))
            except AssertionError:
                print("test case nr. ", i+1, " failed")
                raise AssertionError
if __name__ == "__main__":
    unittest.main()
import unittest
 
class Solution:
    def maxProduct(self, nums) -> int:
        
        candidates = [max(nums)]
        i = 0
        j= 0
        arr = []
        for i in nums:
            if i != 1:
                arr.append(i)
        len_ = len(arr)

        while i < len_ - 1:
            j = i+1
            prev = arr[i]
            while j < len_ :
                val = arr[j]
                mult = prev * val

                candidates.append(mult)
                print(i, j, "val ", val, "prev ", prev, "mult ", mult)

                j += 1
                prev = mult
            i += 1
        print(candidates)
        return max(candidates)



class TestDay11(unittest.TestCase):

    S = Solution()
    test_inp = [
        [2,3,-2,4],
        [1, 2, 3],
        [-2,0,-1],
        [-2,3,-4],
        [-2],
        [0, 2],
        [0,2,3,1,1,1,1],
    ]
    test_result = [
        6,
        1*2*3,
        0,
        24,
        -2,
        2,
        2*3,
    ]

    def test_solution(self):
        for i, val in enumerate(self.test_inp):
            
            try:
                self.assertEqual(self.test_result[i], self.S.maxProduct(val))
            except:
                print("test case nr. ", i+1, " failed")
                raise AssertionError
if __name__ == "__main__":
    unittest.main()


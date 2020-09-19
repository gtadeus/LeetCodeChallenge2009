import unittest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split('.')
        b = version2.split('.')

        return self.compare(a, b)

    def compare(self, a, b):
        ret_val = 0
        if len(a) > 0:
            a1 = int(a.pop(0).strip())
        else:
            a1=0

        if len(b) > 0:
            b1 = int(b.pop(0).strip())
        else:
            b1=0

        #print(a1, b1, a1>b1)
        if (a1 > b1): 
            return 1
        if (a1 < b1):
            return -1
        if (a1 == b1):
            if (len(a)>0 or len(b)>0):
                ret_val = self.compare(a, b)
            else:
                return 0
        
        return ret_val



class TestDay09(unittest.TestCase):

    S = Solution()
    test_inp = [
        {"version1" : "0.1", "version2" : "1.1"},
        {"version1" : "1.0.1", "version2" : "1"},
        {"version1" : "7.5.2.4", "version2" : "7.5.3"},
        {"version1" : "1.01", "version2" : "1.001"},
        {"version1" : "1.0", "version2" : "1.0.0",}
    ]
    test_result = [
        -1,
        1,
        -1,
        0,
        0
    ]

    def test_solution(self):
        for i, val in enumerate(self.test_inp):
            
            try:
                self.assertEqual(self.test_result[i], self.S.compareVersion(val["version1"], val["version2"]))
            except:
                print("test case nr. ", i+1, " failed")
                raise AssertionError
if __name__ == "__main__":
    unittest.main()
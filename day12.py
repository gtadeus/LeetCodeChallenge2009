import unittest
 
class Solution:
    def combinationSum3(self, k: int, n: int):
        p = [i+1 for i in range(k)]
        print(p)
        ret  = []
        for i in range(1, k+1):
            #
            pp = p[-i]
            print('i', i, pp)
            hit = False
            j = pp + (i)
            print(j)
            if sum(p) == n:
                print("s", p)
                ret.append(sorted(p.copy()))
                print(ret)
                p[-i]=pp
                hit = True
            else:
                while not hit and j < 9:
                    p[-i] = j
                    print(p)
                    if sum(p)==n:
                        print("s", p)
                        hit = True
                        
                        ret.append(sorted(p.copy()))
                        print(ret)
                        p[-i]=pp
                    j += 1
        print(ret)
        return ret

        
        



class TestDay11(unittest.TestCase):

    S = Solution()
    test_inp = [
        [3, 7],
        [3, 9],
        [2, 6],
    ]
    test_result = [
        [[1,2,4]],
        [[1,2,6],[1,3,5],[2,3,4]],
        [[1,5], [2,4]]
    ]

    def test_solution(self):
        for i, val in enumerate(self.test_inp):
            
            try:
                self.assertCountEqual(self.test_result[i], self.S.combinationSum3(val[0], val[1]))
            except:
                print("test case nr. ", i+1, " failed")
                raise AssertionError
if __name__ == "__main__":
    unittest.main()

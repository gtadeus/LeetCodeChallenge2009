import unittest
 
class Solution:
    def combinationSum32(self, k: int, n: int):
        ret  = []
        for r in range(n-k):
            p = [i+1 for i in range(r, k+r)]
            print(p)
            for i in range(1, k+1):
                
                pp = p[-i]

                hit = False
                j = pp + (i)
                
                if sum(p) == n:
                    result = sorted(p.copy())
                    if result not in ret:
                        ret.append(result)

                    #p[-i]=pp
                    #hit = True
                else:
                    while not hit and j < 10:
                        
                        p[-i] = j
                        print(p)
                        if sum(p)==n:

                            #hit = True
                            
                            result = sorted(p.copy())
                            if result not in ret:
                                ret.append(result)

                            
                        j += 1
                p[-i]=pp
        print(ret)
        return ret


    def combinationSum3(self, k: int, n: int):
        ret  = []
        i = 10**(k-1)
        
        ind = max(0, (k//2)-3)
        #print(k, ind)
        start = [i for i in range(k, -1, -1)]
        start_i = [val*10**i for (i, val) in enumerate(start)]
        i = sum(start_i)
        #print(sum(start)+1, n)
        check_one=False
        if sum(start)+1 > n:
            finish=True
            check_one = True

        #finish=True
        finish = False
        while i < 10**k and not finish:
            
            nr = str(i)
            p = [-1]*k
            
            for j in range(k):
                p[j] = int(nr[j])
            #print(p)
            
            if not -1 in p and not 0 in p and len(set(p))==k:
                if sum(p)==n:
                    #print(p)
                    result = sorted(p)
                    if not result in ret:
                        ret.append(result)
            if p[ind]==9:
                finish=True
            if check_one:
                #print(p)
                finish=True
            i+=1
                
        #print(ret)
        return ret

    def runner(self, n, k, ret, ind, i, check_one=False):
        
        return ret




class TestDay11(unittest.TestCase):

    S = Solution()
    test_inp = [
        [3, 7],
        [3, 9],
        [2, 6],
        [3, 15],
        [4, 24],
        [5, 15],
        [6, 30],
        [8, 36]
    ]
    test_result = [
        [[1,2,4]],
        [[1,2,6],[1,3,5],[2,3,4]],
        [[1,5], [2,4]],
        [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]],
        [[1,6,8,9],[2,5,8,9],[2,6,7,9],[3,4,8,9],[3,5,7,9],[3,6,7,8],[4,5,6,9],[4,5,7,8]],
        [[1,2,3,4,5]],
        [[1,2,3,7,8,9],[1,2,4,6,8,9],[1,2,5,6,7,9],[1,3,4,5,8,9],[1,3,4,6,7,9],[1,3,5,6,7,8],[2,3,4,5,7,9],[2,3,4,6,7,8]],
        [[1, 2, 3, 4, 5, 6, 7, 8]]
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

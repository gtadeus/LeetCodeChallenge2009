import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        m = self.c(root)
        r=0
        for n in m:
            if n != 0:
                if n== 1:
                    r+=1
                else:
                    r+=int(n,2)
        return r
    def c(self, l):
        if l.left is None and l.right is None:
            return [l.val]
        else:
            p, p2 = [], []
            if not l.left is None:
                p=self.c(l.left)
            if not l.right is None:
                p2=self.c(l.right)
            v=f'{l.val}'
            #v = l.val << 1
            for i, x in enumerate(p):
                if not l.left is None:
                    p[i]=f'{v}{x}'
            for i, x in enumerate(p2):
                if not l.right is None:
                    p2[i]=f'{v}{x}'
                
            return p+p2

        

class TestDay08(unittest.TestCase):
    S = Solution()
    input_ = [ TreeNode(1, TreeNode(0, TreeNode(0,None,None), TreeNode(1,None,None)), TreeNode(1, TreeNode(0,None,None), TreeNode(1,None,None))) ]

    solutions = [22]
    def testSumRoot(self):
        for indx, val in enumerate(self.input_):
            self.assertEqual(self.solutions[indx], self.S.sumRootToLeaf(val))

if __name__ == "__main__":
    unittest.main()
    
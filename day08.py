import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths = self.findPath(root)

        return sum(paths)
    def printChildren(self, nodes):
        for indx, c in enumerate(nodes):
                print("c_", indx, ": ", c.val, c.left, c.right, True)
    def findPath(self, list_, parents = None,  paths=[]):
        children = []
        new_paths = []
        if (len(list_)>0):
            if (parents is None):
                c = TreeNode(list_.pop(0), list_.pop(0), list_.pop(0))
                children.append(c)
                #path = f"{c.val}{c.left}"
                path = c.val * 2**1 + c.left * 2**0
                paths.append(path)
                path = c.val *2**1 + c.right *2**0

                paths.append(path)
            else:
                for p in parents:
                    c = TreeNode(p.left, list_.pop(0), list_.pop(0))
                    children.append(c)
                    c = TreeNode(p.right, list_.pop(0), list_.pop(0))
                    children.append(c)
                    for ind, p in enumerate(paths):
                        #paths[ind] = f"{p}{c.right}"
                        paths[ind] = int(int(bin(p), 2) << 1) + c.right 
                        #path2= f"{p}{c.left}"
                        path2 = int(int(bin(p),2) << 1) + c.left 
                        new_paths.append(path2)

            
            #for indx, c in enumerate(children):
            #    print("c_", indx, ": ", c.val, c.left, c.right, True)
            paths = paths + new_paths
            paths = self.findPath(list_, children, paths)
        
        return paths

class TestDay08(unittest.TestCase):
    S = Solution()
    input_ = [ [1,
                0,1,
                0,1,0,1]
                ]
    solutions = [22]
    def testSumRoot(self):
        for indx, val in enumerate(self.input_):
            self.assertEqual(self.solutions[indx], self.S.sumRootToLeaf(val))

if __name__ == "__main__":
    unittest.main()
    
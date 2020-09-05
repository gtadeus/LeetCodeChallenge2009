import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    def ret_vals(self):
        ret_list = []
        for v in [self.val, self.left, self.right]:
            if (not v is None):
                if (not type(v) is int):
                    ret_list.append(v.ret_vals())
                else:
                    ret_list.append(v)

        return ret_list

def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]
def func(root1, root2):
    
    list1 = flatten(root1.ret_vals())
    list2 = flatten(root2.ret_vals())
    
    return sorted(list1+list2)
    #return 

root1 = TreeNode(2,1,4)
root2 = TreeNode(1,0,3)
root3 = TreeNode(0, -10, 10)
root4 = TreeNode(5,None,TreeNode(7,0,2))
print(func(root1, root2))
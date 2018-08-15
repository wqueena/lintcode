"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # write your code here
        if self.preorder(a,[])==self.preorder(b,[]) and self.order(a,[])==self.order(b,[]):
            return True
        return False
    
    def preorder(self,root,res):
        if root is None:
            return
        res.append(root.val)
        self.preorder(root.left,res)
        self.preorder(root.right,res)
        return res
    
    def order(self,root,res):
        if root is None:
            return 
        self.order(root.left,res)
        res.append(root.val)
        self.order(root.right,res)
        return res

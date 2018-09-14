"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def depth(self,root):
        if root is None:
            return 0
        return 1+max(self.depth(root.left),self.depth(root.right))
    def diameterOfBinaryTree(self, root):
        # write your code here
        return self.depth(root.left)+self.depth(root.right)

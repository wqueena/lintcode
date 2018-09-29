"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a root of integer
    @return: return a list of integer
    """

    def largestValues(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        node = []
        node.append(root)
        while node:
            result.append(max(i.val for i in node))
            temp = []
            for each in node:
                if each.left:
                    temp.append(each.left)
                if each.right:
                    temp.append(each.right)
            node = temp
        return result

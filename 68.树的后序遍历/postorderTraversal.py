class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insertLeft(self, item):
        if self.left is None:
            self.left = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.left = self.left
            self.left = t

    def insertRight(self, item):
        if self.right is None:
            self.right = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.right = self.right
            self.right = t


def build_tree_with_post():
    tree = BinaryTree(1)
    tree.insertRight(2)
    tree.right.insertLeft(3)
    return tree


out = []


class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return
        else:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
        out.append(root.val)
        return out


if __name__ == '__main__':
    so = Solution()
    print(so.postorderTraversal(build_tree_with_post()))

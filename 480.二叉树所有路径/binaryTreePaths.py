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
    tree.insertLeft(-5)
    tree.insertRight(2)
    tree.left.insertLeft(0)
    tree.left.insertRight(3)
    tree.right.insertLeft(-4)
    tree.right.insertRight(-5)
    return tree


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        out = []
        temp = []
        if root is None:
            return out
        return self.find(root, out, temp)

    def find(self, root, out, temp):
        temp.append(str(root.val))
        if root.left is None and root.right is None:
            out.append('->'.join(temp))
            temp.pop()
            return
        if root.left:
            self.find(root.left, out, temp)
        if root.right:
            self.find(root.right, out, temp)
        temp.pop()
        return out


if __name__ == '__main__':
    so = Solution()
    print(so.binaryTreePaths(build_tree_with_post()))

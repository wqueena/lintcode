class Node(object):
    """节点类"""

    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None

    def insertLeft(self, item):
        if self.left is None:
            self.left = Node(item)
        else:
            t = Node(item)
            t.left = self.left
            self.left = t

    def insertRight(self, item):
        if self.right is None:
            self.right = Node(item)
        else:
            t = Node(item)
            t.right = self.right
            self.right = t


class Tree(object):
    """树类"""

    def build_tree(self):  # 建树
        self.tree = Node(1)
        self.tree.insertLeft(-5)
        self.tree.insertRight(2)
        self.tree.left.insertLeft(3)
        return self.tree

    def preorder_digui(self, root, result):  # 用递归实现前序遍历
        if root is None:
            return
        result.append(root.val)
        self.preorder_digui(root.left, result)
        self.preorder_digui(root.right, result)
        return result

    def inorder_digui(self, root, result):  # 用递归实现中序遍历
        if root is None:
            return
        self.inorder_digui(root.left, result)
        result.append(root.val)
        self.inorder_digui(root.right, result)
        return result

    def postorder_digui(self, root, result):  # 用递归实现后序遍历
        if root is None:
            return
        self.postorder_digui(root.left, result)
        self.postorder_digui(root.right, result)
        result.append(root.val)
        return result

    def preorder_stack(self, root, result):  # 用栈实现前序遍历
        if root is None:
            return
        _stack = []
        while _stack or root:
            while root:
                result.append(root.val)
                _stack.append(root)
                root = root.left
            root = _stack.pop()
            root = root.right
        return result

    def inorder_stack(self, root, result):  # 用栈实现中序遍历
        if root is None:
            return
        _stack = []
        while _stack or root:
            while root:
                _stack.append(root)
                root = root.left
            root = _stack.pop()
            result.append(root.val)
            root = root.right
        return result

    def postorder_stack(self, root, result):  # 用栈实现后序遍历
        if root is None:
            return
        _stack = [root]
        while _stack:
            root = _stack.pop()
            if root.left:
                _stack.append(root.left)
            if root.right:
                _stack.append(root.right)
            result.append(root.val)

        result.reverse()
        return result

    def level_queue(self, root, result):  # 用队列实现层次遍历
        if root is None:
            return
        _queue = [root]
        while _queue:
            root = _queue.pop(0)
            result.append(root.val)
            if root.left:
                _queue.append(root.left)
            if root.right:
                _queue.append(root.right)
        return result


if __name__ == '__main__':
    """主函数"""
    tr = Tree()
    print(tr.preorder_digui(tr.build_tree(), []))
    print(tr.inorder_digui(tr.build_tree(), []))
    print(tr.postorder_digui(tr.build_tree(), []))
    print(tr.preorder_stack(tr.build_tree(), []))
    print(tr.inorder_stack(tr.build_tree(), []))
    print(tr.postorder_stack(tr.build_tree(), []))
    print(tr.level_queue(tr.build_tree(), []))

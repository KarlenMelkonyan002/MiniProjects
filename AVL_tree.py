class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, root):
        if not root:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        a.height = 1 + max(self.get_height(a.left), self.get_height(a.right))
        return a

    def left_rotate(self, node):
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        a.height = 1 + max(self.get_height(a.left), self.get_height(a.right))
        return a

    def insert(self, val, root):
        if not root:
            return Node(val)
        elif val <= root.value:
            root.left = self.insert(val, root.left)
        else:
            root.right = self.insert(val, root.right)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and val < root.left.value:
            return self.right_rotate(root)
        if balance < -1 and val > root.right.value:
            return self.left_rotate(root)
        if balance > 1 and val > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and val < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def clear(self, root):
       if root is not None:
           self.clear(root.left)
           self.clear(root.right)
           del root

    def erase(self):
        pass

    def get_number_of_nodes(self, root):
        if not root:
            return 0
        return 1 + self.get_number_of_nodes(root.left) + self.get_number_of_nodes(root.right)

    def preorder(self, root):
        if not root:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value)
        pass

    def levelorder(self):
        pass

    def get_root_data(self, root):
        return root.value

    def merge(self):
        pass

    def contains(self, node, key):
        if not node:
            return False
        if node.value == key:
            return True
        ans1 = self.contains(node.left, key)
        if ans1:
            return True
        ans2 = self.contains(node.right, key)
        return ans2

    def find(self):
        pass


Tree = AVLTree()
root_ = None
root_ = Tree.insert(10, root_)
root_ = Tree.insert(20, root_)
root_ = Tree.insert(30, root_)
root_ = Tree.insert(40, root_)
root_ = Tree.insert(50, root_)
root_ = Tree.insert(25, root_)

Tree.preorder(root_)
# Tree.inorder(root_)
print(Tree.get_height(root_))

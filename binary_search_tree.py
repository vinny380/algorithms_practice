""" Must have an insert (self, value) function that inserts a new
node with a given value into the BST. You may assume that the values to
be stored in the tree are integers."""

class tree_node:
    def __init__(self, value):
        self.value = int(value)
        self.right = self.left = None

class BST:
    def __init__(self, root):
        self.root = tree_node(root)
    
    def insert(self, value):
        start = self.root
        new_node = tree_node(value)
        acc = None

        while start != None:
            acc = start

            if value > start.value:
                start = start.right
            elif value < start.value:
                start = start.left

            
        if acc == None:
            acc = new_node
        elif (value < acc.value):
            acc.left = new_node
        else:
            acc.right = new_node
        
        return acc


    def max_value(self):
        start = self.root
        while start.right:
            start = start.right
            if start.right == None:
                acc = start
        return acc.value

    def min_value(self):
        start = self.root
        while start.left:
            start = start.left
            if start.left == None:
                acc = start
        return acc.value

    def traversal(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")

    def preorder_print(self, start, traversal):
        if start != None:
            traversal = traversal + str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start != None:
            traversal = self.preorder_print(start.left, traversal)
            traversal = traversal + str(start.value) + "-"
            traversal = self.preorder_print(start.right, traversal)
        return traversal     

tree = BST(10)
tree.insert(30)
tree.insert(25)
tree.insert(50)
print(tree.max_value())

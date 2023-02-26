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

        while start != None:
            if value > start.value:
                start = start.right
            elif value < start.value:
                start = start.left
            else:
                break

            if start == None:
                start = new_node

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

tree = BST(10)
tree.insert(30)
print(tree.max_value)

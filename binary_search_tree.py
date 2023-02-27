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
        if start.right == None and start.left == None:
            return start.value
        if start.right == None:
            return start.value
        while start.right:
            start = start.right
            if start.right == None:
                acc = start
        return acc.value

    def min_value(self):
        start = self.root
        if start.right == None and start.left == None:
            return start.value
        if start.left == None:
            return start.value
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

    def delete(self, value, start):
        acc = None 
        if start.value == value:
            if start.right != None:
                acc = start.right
            elif (start.right == None) and start.left != None:
                acc = start.left
            else:
                acc = None
            return acc
        if value > start.value:
            start = self.delete(value, start.right)
        elif value < start.value:
            start = self.delete(value, start.left)
        else:
            raise Exception("Number not in tree")
        return acc

    def save(self):
        bst_string = self.traversal('preorder')
        return bst_string

    def restore(self, input_string):
        input_string_list = input_string.rsplit("-")
        del input_string_list[len(input_string_list)-1]

        f = BST(input_string_list[0])
        f.insert(13)
        for n in input_string_list:
            f.insert(n)
        return f

if __name__ == '__main__':
    tree = BST(10)
    tree.insert(30)
    tree.insert(6)
    tree.insert(100)
    tree.insert(25)
    tree.insert(50)
    # tree.delete(100, tree.root)
    n = tree.save()
    restored = tree.restore(n)
    restored.insert(49)
    print(restored.traversal('inorder'))

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
            if new_node.value > start.value:
                start = start.right
            elif new_node.value < start.value:
                start = start.left
            
        if acc == None:
            acc = new_node
        elif (new_node.value < acc.value):
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
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")


    def preorder_print(self, start, traversal):
        if start != None:
            traversal = traversal + str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


    def inorder_print(self, start, traversal):
        if start != None:
            traversal = self.inorder_print(start.left, traversal)
            traversal = traversal + str(start.value) + "-"
            traversal = self.inorder_print(start.right, traversal)
        return traversal     


    def delete(self, value):
        self.root = self.delete_recursive(self.root, value)


    def delete_recursive(self, start, value):
        if start is None:
            return None
        
        if value > start.value:
            start.right = self.delete_recursive(start.right, value)
        elif value < start.value:
            start.left = self.delete_recursive(start.left, value)
        else: # start.value == value
            if start.right is None:
                return start.left
            elif start.left is None:
                return start.right
            else: # start has two children
                current = start.right
                while current.left is not None:
                    current = current.left
                start.value = current.value
                start.right = self.delete_recursive(start.right, current.value)
        return start



    def save(self):
        bst_string = self.traversal('preorder')
        return bst_string


    def restore(self, input_string):
        # input_string must be the preorder version of the tree.
        input_string_list = input_string.rsplit("-")
        del input_string_list[len(input_string_list)-1]
        root = input_string_list[0]
        tree = BST(root)
        del input_string_list[0]
        tree.insert(45)
        for n in input_string_list:
            tree.insert(n)
        return tree
    
    
    def get_total_height(self):
        pass

if __name__ == '__main__':
    tree = BST(10)
    tree.insert(30)
    tree.insert(6)
    tree.insert(100)
    tree.insert(25)
    tree.insert(50)

    tree.delete(30)
    # n = tree.save()
    # restored = tree.restore(n)
    # restored.insert(49)
    # restored.insert(1000)
    print(tree.root.value)
    print(tree.traversal('preorder'))

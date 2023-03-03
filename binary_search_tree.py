class tree_node:
    def __init__(self, value):
        self.value = int(value)
        self.right = self.left = None


class BST:
    def __init__(self, root):
        self.root = tree_node(root)


    '''Inserts a new value to the tree.'''
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


    '''Finds the greatest value in the tree.'''
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


    '''Finds the lowest value in the tree.'''
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


    '''Returns a string version of the tree
    traversal_type has 3 options - preorder, inorder, postorder
    '''
    def traversal(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:       # Raises exception in case the user gives a non-acceptable parameter.
            raise Exception('''Choose a valid traversal type:\n
            * preorder\n
            * inorder\n
            * postorder
            ''')


    '''Performs a preorder print'''
    def preorder_print(self, start, traversal):
        if start != None:
            traversal = traversal + str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


    '''Performs an inorder print'''
    def inorder_print(self, start, traversal):
        if start != None:
            traversal = self.inorder_print(start.left, traversal)
            traversal = traversal + str(start.value) + "-"
            traversal = self.inorder_print(start.right, traversal)
        return traversal     


    '''Performs a postorder print'''
    def postorder_print(self, start, traversal):
        if start != None:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal = traversal + str(start.value) + "-"
        return traversal             


    '''Deletes a value in the tree starting from the root'''
    def delete(self, value):
        self.root = self.__delete_recursive(self.root, value)


    def __delete_recursive(self, start, value):
        if start is None:
            return None
        
        if value > start.value:
            start.right = self.__delete_recursive(start.right, value)
        elif value < start.value:
            start.left = self.__delete_recursive(start.left, value)
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
                start.right = self.__delete_recursive(start.right, current.value)
        return start


    '''Saves the tree as a string in a preorder traversal'''
    def save(self):
        bst_string = self.traversal('preorder')
        return bst_string


    '''Transforms a string into a tree.
    input_string must be the preorder version of the tree.
    '''
    def restore(self, input_string):
        # input_string must be the preorder version of the tree.
        input_string_list = input_string.rsplit("-")        # Turning the string into a list
        del input_string_list[len(input_string_list)-1]     # Deleting the last element, because it is ''
        root = input_string_list[0]                         # Setting the first element of the list as the root.
        tree = BST(root)                                    # It works because it was saved as preorder traversal.
        del input_string_list[0]                            # Deleting the root.                                     
        for n in input_string_list:                         # Adding all other elements to the tree.
            tree.insert(n)
        return tree
    

    '''Returns the height of the whole tree'''
    def get_total_height(self):
        return self.__get_total_height_recursive(self.root)
        

    '''Returns the height of a given node'''
    def __get_total_height_recursive(self, start):
        if start is None:
            return 0
        else:
            # Compute the height of each subtree
            left_height = self.__get_total_height_recursive(start.left)
            right_height = self.__get_total_height_recursive(start.right)

            return max(left_height, right_height) + 1


if __name__ == '__main__':
    tree = BST(10)
    tree.insert(30)
    tree.insert(6)
    tree.insert(100)
    tree.insert(25)
    tree.insert(50)
    tree.delete(30)
    n = tree.save()     #n is of type<str>
    restored = tree.restore(n)
    restored.insert(49)
    restored.insert(1000)
    print(restored.traversal('preorder'))   # It should return 10-6-45-25-50-49-100-1000
    print(restored.get_total_height())      # It should return 5
    print(f"Min value - {restored.min_value()}\nMax value - {restored.max_value()}")

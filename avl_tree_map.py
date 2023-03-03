import re
import string
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
def parse_file(file):
    with open(file, 'r') as input:
        content = input.readlines()
    preprocessed = []
    for line in content:
        line = line.strip().lower()
        #remove punctuation
        line = line.translate(str.maketrans('', '', string.punctuation))
        #remove stop words that care no specific meaning
        line = remove_stopwords(line)
        #remove numbers
        line = re.sub('\d+','', line)
        #remove extra white space
        line = re.sub(' +', ' ', line)
        if line:
            preprocessed.extend(line.split(" "))
    print(" ".join(preprocessed))
    return preprocessed

def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stop_words])

'''All nodes will have a value, left and right children (This could be None) and frequency.'''
class  AVLTreeMapNode:
    def __init__(self, word):
        self.value = str(word)
        self.left = self.right = None
        self.frequency = self.height = 1


class AVLTreeMap:
    def __init__(self):
        self.root = None


    '''Inserts a value in the tree'''
    def insert(self, value):
        self.root = self.__insert_recursive(self.root, value)
        
    
    '''Inserts a value in the tree starting from a given node'''
    def __insert_recursive(self, node, value):
        # Perform regular BST insertion
        if node == None:
            return AVLTreeMapNode(value)
        elif value < node.value:
            node.left = self.__insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self.__insert_recursive(node.right, value)
        else:
            node.frequency += 1
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))   # Update the height of the current node
        
        balance = self.balance(node)        # Check if the node is balanced
        
        # If the node is unbalanced, balance it
        if balance > 1:
            if self.balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif balance < -1:
            if self.balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
        

    '''Returns the new root when a left rotation is performed'''    
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        
        return new_root        


    '''Returns the new root when a right rotation is performed'''
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        
        return new_root
    

    '''Returns the height of a given node'''
    def height(self, node):
        if node == None:
            return 0
        return node.height


    '''Returns the balance of a given node'''    
    def balance(self, node):
        if node == None:
            return 0
        return self.height(node.left) - self.height(node.right)


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
            traversal = print(f"{start.value}, {start.frequency}\n", end=" ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


    '''Performs an inorder print'''
    def inorder_print(self, start, traversal):
        if start != None:
            traversal = self.inorder_print(start.left, traversal)
            traversal = print(f"{start.value}, {start.frequency}\n", end=" ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal  


    '''Performs a postorder print'''
    def postorder_print(self, start, traversal):
        if start != None:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal = print(f"{start.value}, {start.frequency}\n", end=" ")
        return traversal  


    '''Returns an AVL Tree (avl_tree)
    file_path is a string.
    '''
    def load_from_file(self, file_path):
        words = parse_file(file_path)
        avl_tree = AVLTreeMap()         # Creating instance of tree
        for word in words:              # Adding all the words in the list words to the tree.
            avl_tree.insert(word)
        return avl_tree

if __name__ == "__main__":
    tree = AVLTreeMap()

    #test.txt contains: Binary search tree is a special binary tree
    j = tree.load_from_file('test.txt')
    '''It prints:
    search, 1
    binary, 2
    tree, 2
    special, 1
    '''
    print(j.traversal('preorder'))


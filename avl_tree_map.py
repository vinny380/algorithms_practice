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


class  AVLTreeMapNode:
    def __init__(self, word):
        self.value = word
        self.left = self.right = None
        self.frequency = self.height = 1

class AVLTreeMap:
    def __init__(self,root):
        self.root = AVLTreeMapNode(root)

    def insert(self, value):
        self.root = self.insert_helper(self.root, value)
        
    def insert_helper(self, node, value):
        # Perform regular BST insertion
        if not node:
            return AVLTreeMapNode(value)
        elif value < node.value:
            node.left = self.insert_helper(node.left, value)
        elif value > node.value:
            node.right = self.insert_helper(node.right, value)
        else:
            node.frequency += 1
        
        # Update the height of the current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        # Check if the node is balanced
        balance = self.get_balance(node)
        
        # If the node is unbalanced, balance it
        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
        
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        
        return new_root
        
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        
        return new_root
        
    def get_height(self, node):
        if not node:
            return 0
        return node.height
        
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
        
    def print_tree(self):
        if not self.root:
            return
        self.print_helper(self.root)
        
    def print_helper(self, node):
        if node:
            self.print_helper(node.left)
            print("{0}, {1}\n".format(node.value, node.frequency), end=" ")
            self.print_helper(node.right)

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


    ''' 
    This function aims to read content from 
    a file and save word-frequency information
    for all words appearing in the file in the AVLTreeMap
    '''
def load_from_file(file_path):
    words = parse_file(file_path)
    avl_tree = AVLTreeMap(words[0])
    for word in words[1:]:
        avl_tree.insert(word)
    return avl_tree.traversal("inorder")


if __name__ == "__main__":
    load_from_file('test.txt')

class tree_node:
  def __init__(self, value):
    self.value = value
    self.right = self.left = None

class tree:
  def __init__(self, root):
    self.root = tree_node(root)

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

  def max_value(self):
    start = self.root
    while start.right:
        start = start.right
        if start.right == None:
          acc = start
    return acc.value


tree = tree(10)
tree.root.left = tree_node(5)
tree.root.right = tree_node(20)
tree.root.left.left = tree_node(3)
tree.root.left.right = tree_node(7)
tree.root.right.left = tree_node(17)
tree.root.right.right = tree_node(22)
tree.root.right.right.right= tree_node(44)
print(tree.max_value())

# NLR
#10 - 5 - 3 - 7 - 20 - 17 - 22
#LNR
#3 - 5 - 7 - 10 - 17 - 20 - 22 

# tree.traversal('inorder')
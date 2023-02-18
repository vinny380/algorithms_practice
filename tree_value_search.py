'''
Create a recursive algorithm that takes a binary search tree T
and a value x and returns the smallest value in T, which is >= x.
If there is no such value, your algorithm should return "Not found".

For example, if your tree contains the values {1,2,5,10,12} and x = 9,
the algorithm should return 10. If x = 20, the algorithm should return "None". 
'''

from tree import tree_node, tree

def smallest_value_greater_than_x(T: tree, x: float):
    root = T.root
    if root.value > x:
        while root.value > x:
            acc = root.left
            if acc.left.value < x:
                break
            acc = smallest_value_greater_than_x(acc.left, x)
    elif root.value < x:
        while root.value > x:
            acc = root.right
            if acc.right.value > x:
                break
            acc = smallest_value_greater_than_x(acc.right, x)
    elif root.value == x:
        acc = root
    else:
        acc = None
    return acc


   

    
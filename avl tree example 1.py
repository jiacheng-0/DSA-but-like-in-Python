
from avl_tree import *

# explore restructuring process

myTree = AVL_Tree()
root = None

inserts = [30, 40, 24, 58, 48, 26, 11, 13, 19]
for one_item in inserts:
    root = myTree.insert(root, one_item)

# Inorder Traversal
    print("Inorder traversal of the", "constructed AVL tree is")
    myTree.inOrder(root)
    print()
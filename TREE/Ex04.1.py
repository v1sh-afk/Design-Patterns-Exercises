from TreeNode import Tree
from BinaryTree import BinaryTree
from BinarySearchTree import BinarySearchTree
from heap import Heap
from avl import AVLTree


#BT = BinaryTree(11)
BST = BinarySearchTree(0)
avl = AVLTree(0)
h = Heap(0)

l = [i for i in range(10)]
for i in l:
    #BT.insertion(i)
    BST.insertion(i)
    #avl.insertion(i)

#BT.preorder()
BST.inorder()
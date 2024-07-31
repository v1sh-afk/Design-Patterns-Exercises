from  BinaryTree import BinaryTree
from TreeNode import Tree

class BinarySearchTree(BinaryTree):
    def __init__(self,data) -> None:
        super().__init__(data)

    def insertion(self, data):
        if not self.data:
            self.data = data
            return
        else:
            if self.data < data:
                if self.lchild:
                    self.lchild.insertion(data)
                else:
                    self.lchild = BinarySearchTree(data)

            if self.data > data:
                if self.rchild:
                    self.rchild.insertion(data)
                else:
                    self.rchild = BinarySearchTree(data)

    
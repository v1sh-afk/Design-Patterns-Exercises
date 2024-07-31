from abc import ABC,abstractclassmethod

class Tree(ABC):
    
    def __init__(self,data) -> None:
        self.data = data
        self.lchild = None
        self.rchild = None
        self.height = 0

    @abstractclassmethod
    def insertion(self,data):
        raise NotImplementedError("Function Doesn't Implemented")
    
    @abstractclassmethod
    def is_leaf(self):
        raise NotImplementedError("Function Doesn't Implemented")

    @abstractclassmethod
    def is_root(self):
        raise NotImplementedError("Function Doesn't Implemented")

    @abstractclassmethod
    def is_parent(self):
        raise NotImplementedError("Function Doesn't Implemented")
    
    @abstractclassmethod
    def search(self):
        raise NotImplementedError("Function Doesn't Implemented")
    
    @abstractclassmethod
    def preorder(self):
        raise NotImplementedError("Function Doesn't Implemented")
    
    @abstractclassmethod
    def inorder(self):
        raise NotImplementedError("Function Doesn't Implemented")
    
    @abstractclassmethod
    def postorder(self):
        raise NotImplementedError("Function Doesn't Implemented")


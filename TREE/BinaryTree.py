from TreeNode import Tree


class BinaryTree(Tree):

    def __init__(self,data) -> None:
        super().__init__(data)
    
    def insertion(self, data):
       if self.data is None:
          self.data = data
          return
       q= [self]
       while len(q)>0:
            n=q.pop()
            if not n.lchild:
                n.lchild = BinaryTree(data)
                return
            if not n.rchild:
                n.rchild = BinaryTree(data)
                return
            q.append(self.lchild)
            q.append(self.rchild)

    def delete(self,k):
        q=[self]
        while(len(q)>0):
            n=q.pop()
            if (n and n.data==k):
                while(n.lchild):
                    n.lchild,n=n,n.lchild
                    n=n.lchild
                n.parent.lchild=None
                return
            if (n.lchild):
                q.append(n.lchild)
            if (n.rchild):
                q.append(n.rchild)

    def search(self,data):
        q=[self]
        while(len(q)>0):
            n=q.pop()
            if (n and n.data==data):
                print("Element exist in the Tree")
                return 
            if (n.lchild):
                q.append(n.lchild)
            if (n.rchild):
                q.append(n.rchild)

    def is_leaf(self,data):
        q=[self]
        while(len(q)>0):
            n=q.pop()
            if (n and n.data==data):
                if not(n.lchild or n.rchild):
                     return True
                else:
                     return False
            if (n.lchild):
                q.append(n.lchild)
            if (n.rchild):
                q.append(n.rchild)

    def is_root(self,data):
        return self.data == data        

    def is_parent(self,data):
        q=[self]
        while(len(q)>0):
            n=q.pop()
            if (n and n.data==data):
                if (n.lchild or n.rchild):
                     return True
                else:
                     return False
            if (n.lchild):
                q.append(n.lchild)
            if (n.rchild):
                q.append(n.rchild)

    def preorder(self):
        print(self.data,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data,end=" ")
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.child.preorder()
        if self.rchild:
            self.rchild.preorder()
        print(self.data,end=" ")




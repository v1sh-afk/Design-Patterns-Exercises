class Heap:
    def __init__(self,capacity=9000):
        self.array=[None]*capacity
        self.capacity=capacity
        self.size=0
    def getParentIndex(self,index):
        return(index-1)//2
    def getLeftChildIndex(self,index):
        return (2*index)+1
    def getRightChildIndex(self,index):
        return(2*index)+2
    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index)<self.size
    def hasRightChild(self,index):
        return self.getRightChildIndex(index)<self.size
    def isFull(self):
        return self.size==self.capacity
    def swap(self,index1,index2):
        self.array[index1],self.array[index2]=self.array[index2],self.array[index1]
    def parent(self,index):
        return self.array[self.getParentIndex(index)]
    def leftchild(self,index):
        return self.array[self.getLeftChildIndex(index)]
    def rightchild(self,index):
        return self.array[self.getRightChildIndex(index)]
    def insert(self,data):
        if self.isFull():
            raise "Heap is Full"
        self.array[self.size]=data
        self.size+=1
        self.heapifyUp(self.size-1)
    def heapifyUp(self,index):
        if self.hasParent(index) and self.parent(index)>self.array[index]:
            self.swap(self.getParentIndex(index),index)
            self.heapifyUp(self.getParentIndex(index))
    def replace(self,data,a):
        if self.size==0:
            raise "Empty Heap"
        for i in range(1,self.size):
            if self.array[i]==data:
                index=i
        d=(a,data[1])
        self.array[index]=d
        self.heapifyUp(0)
    def heapifyDown(self,index):
        smallest=index
        if self.hasLeftChild(index) and self.array[smallest]>self.leftchild(index):
            smallest=self.getLeftChildIndex(index)
        if self.hasRightChild(index) and self.array[smallest]>self.rightchild(index):
            smallest=self.getRightChildIndex(index)
        if smallest!=index:
            self.swap(index,smallest)
            self.heapifyDown(smallest)
    def __str__(self):
        return str(self.array)
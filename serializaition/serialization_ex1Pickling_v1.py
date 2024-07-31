#Serialization of multiple objects using Pickle"
import unittest
import pickle

b1={'pid':202201,'name':'XYZ','age':70}
b2={'pid':202202,'name':'ABC','age':50}

with open('file2.txt','wb') as f1:
    pickle.dump([b1,b2],f1)

with open('file2.txt','rb') as f1:
    b1_new=pickle.load(f1)

print(b1_new)




'''
class Hospital():
    def __init__(self,pid,name,age):
        self.pid=pid
        self.name=name
        self.age=age
    def display(self):
        print("Patient {} details: Name {} and age {}".format(self.pid,self.name,self.age))
'''




'''
#To print the attributes
print(b1_new.pid)
print(b1_new.name)
print(b1_new.age)


#Serializing and deserializing the 2nd object to the same file
with open('file2.txt','wb') as f1:
    pickle.dump(b2,f1)
    
with open('file2.txt','rb') as f1:
    b1_new=pickle.load(f1)

b1_new.display()
'''

    

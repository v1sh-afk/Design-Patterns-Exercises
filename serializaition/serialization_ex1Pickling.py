#Serialization of object using Pickle"

import pickle

class Hospital():
    def __init__(self,pid,name,age):
        self.pid=pid
        self.name=name
        self.age=age
    def display(self):
        print("Patient {} details: Name {} and age {}".format(self.pid,self.name,self.age))


b1=Hospital(202201,"XYZ",70)
b2=Hospital(202202,"ABC",50)

with open('file2.txt','wb') as f1:
    pickle.dump(b1,f1)

with open('file2.txt','rb') as f1:
    b1_new=pickle.load(f1)

#To print the attributes
print(b1_new.pid)
print(b1_new.name)
print(b1_new.age)

b1_new.display()


#Serializing and deserializing the 2nd object to a different file

with open('file2.txt','wb') as f2:
    pickle.dump(b2,f2)
    
with open('file2.txt','rb') as f2:
    b2_new=pickle.load(f2)
    
#To print the attributes
print(b2_new.pid)
print(b2_new.name)
print(b2_new.age)


b2_new.display()


'''

#Serializing and deserializing the 2nd object to the same file
#Overwrites the already existing object

with open('file2.txt','wb') as f1:
    pickle.dump(b2,f1)
    
with open('file2.txt','rb') as f1:
    b1_new=pickle.load(f1)
    
#To print the attributes
print(b1_new.pid)
print(b1_new.name)
print(b1_new.age)


b1_new.display()
'''
    

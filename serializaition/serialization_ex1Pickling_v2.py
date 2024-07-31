#Serialization - Displays the output as dict 

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
    pickle.dump([b1,b2],f1)

with open('file2.txt','rb') as f1:
    b1_new=pickle.load(f1)

for patients in b1_new:
    print(patients.__dict__)



'''To print the attributes
print(b1_new.pid)
print(b1_new.name)
print(b1_new.age)
'''
'''
#Serializing and deserializing the 2nd object to the same file
with open('file2.txt','wb') as f1:
    pickle.dump(b2,f1)
    
with open('file2.txt','rb') as f1:
    b1_new=pickle.load(f1)
    
b1_new.display()
'''
    

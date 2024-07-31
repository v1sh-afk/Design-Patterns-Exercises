#Vishal Prakash
f=open("Vishal-UIT2312-ex-04.zip\CODE\iris.txt","r")
#sepal_length,sepal_width,petal_length,petal_width,species
d={"Iris-setosa":[],"Iris-versicolor":[],"Iris-virginica":[]}
b1=[]
d1=[]
for i in f.readlines():
     c=i.split()
     if c[-1]!="class":
        if c[-1] in d:
            d[c[-1]].append(c[:len(c)-1])
class Iris_plant():
    def __init__(self,plant):
        self.plant=plant
class Eucledian_distance(Iris_plant):
    def __init__(self,plant):
        super().__init__(plant)
    def distance(self):
        main=[]
        for i in d:
            temp=[]
            for j in d[i]:
                c=0
                for k in range(len(j)):
                    c=c+((self.plant[k]-float(j[k]))**2)
                if temp==[]:
                    temp.append(c**0.5)
                else:
                    if (c**0.5)<temp[0]:
                        temp[0]=(c**0.5)
            main.append(temp[0])
        dk=min(main)
        if main.index(dk)==0:
            print("The Iris plant comes under class Iris-setosa")
        elif main.index(dk)==1:
            print("The Iris plant comes under class Iris-versicolor")
        else:
            print("the Iris plant comes under class Iris-virginica")
class Manhattan_distance():
    def __init__(self,plant,check):
        self.plant=plant
    def distance(self):
        if self.plant.index(0)>1:
            for i in d:
                b=[]
                for j in d[i]:
                    c=0
                    for k in range(2,len(j)):
                        c=c+abs(self.plant[k]-float(j[k]))
                    if b==[]:
                        b.append(c)
                    else:
                        if c<b[0]:
                            b[0]=c
                d1.append(b[0])
        else:
            for i in d:
                b=[]
                for j in d[i]:
                    c=0
                    for k in range(0,2):
                        c=c+abs(self.plant[k]-float(j[k]))
                    if b==[]:
                        b.append(c)
                    else:
                        if c<b[0]:
                            b[0]=c
                d1.append(b[0])
class Chebysev_distance():
    def __init__(self,plant):
        self.plant=plant
    def distance(self):
         if self.plant.index(0)>1:
            for i in d:
                b=[]
                for j in d[i]:
                    c=[]
                    for k in range(2,len(j)):
                        c.append(abs(self.plant[k]-float(j[k])))
                    if b==[]:
                        b.append(max(c))
                    else:
                        if max(c)<b[0]:
                            b[0]=max(c)
                d1.append(b[0])
         else:
             for i in d:
                b=[]
                for j in d[i]:
                    c=[]
                    for k in range(0,2):
                        c.append(abs(self.plant[k]-float(j[k])))
                    if b==[]:
                        b.append(max(c))
                    else:
                        if max(c)<b[0]:
                            b[0]=max(c)
                d1.append(b[0])
class Soresen_distance(Manhattan_distance,Chebysev_distance):
    def __init__(self,plant):
        self.plant=plant
    def distance(self):
        if self.plant.index(0)>1:
            total=-1
            for i in d:
                total+=1
                b=[]
                for j in d[i]:
                    c=0
                    for k in range(2,len(j)):
                       c+=self.plant[k]+float(j[k])
                    if b==[]:
                        b.append(d1[total]/c)
                    else:
                        if (d1[total]/c)<b[0]:
                            b[0]=d1[total]/c
                d1.append(b[0])
        else:
             total=-1
             for i in d:
                b=[]
                total+=1
                for j in d[i]:
                    c=0
                    for k in range(0,2):
                        c+=self.plant[k]+float(j[k])
                    if b==[]:
                        b.append(d1[total]/c)
                    else:
                        if (d1[total]/c)<b[0]:
                            b[0]=d1[total]/c
                d1.append(b[0])
    def check(self):
        Manhattan_distance.distance(self)
        Chebysev_distance.distance(self)
        self.distance()
        if d1.index(min(d1))==0:
            print("The Iris plant comes under class Iris-setosa")
        elif d1.index(min(d1))==1:
            print("The Iris plant comes under class Iris-versicolor")
        else:
            print("the Iris plant comes under class Iris-virginica")
            
print(
'''
1.2D
2.4D''') 

ch=int(input("enter choice"))
if ch==1:
    print("1.Sepal,2.Petal")
    b=int(input("enter feature"))
    if b==2:
        x=input("enter length and width").split()
        for i in range(len(x)):
            x[i]=int(x[i])
        k=[0,0]
        k.extend(x)
    else:
        x=input("enter length and width").split()
        for i in range(len(x)):
            x[i]=int(x[i])
        k=x
        k.extend([0,0])
    p1=Soresen_distance(k)
    p1.check()
else:
    x=input("enter dimensions").split()
    for i in range(len(x)):
        x[i]=int(x[i])
    k=x
    p1=Eucledian_distance(k)
    p1.distance()
    

        

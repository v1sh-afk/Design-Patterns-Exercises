#Singleton
class PplAsn:
    _instance=None

    def __init__(self):
        if PplAsn._instance==None:
            self.lst=[]
            PplAsn._instance=True
        else:
            raise Exception("This Object is already instantiated!")
        
    def __str__(self):
        return str(self.lst)

    def append(self,obj):
        self.lst.append(obj)

    def search(self,type,term):
        if type=="c":
            self.category_search(term)
        elif type=="n":
            self.name_search(term)

    def category_search(self,term):
        res=False
        for i in self.lst:
            if term in i.category:
                print(i)   
                res=True
        if not res:
            print("NO RESULTS FOUND!")

    def name_search(self,term):
        res=False
        for i in self.lst:
            if term in i.name:
                print(i)   
                res=True
        if not res:
            print("NO RESULTS FOUND!")
    
    def update_salary(self,role,inc):
        for i in self.lst:
            if i.category[0]==role:
                i.salary+=inc
    
    def add_fields(self,role,name,new):
        if role=="HOD" or role=="dean":
            for i in self.lst:
                if i.name==name:
                    i.category.append(new)
        else:
            raise ValueError("You are not a HOD or Dean! You can't add new fields!")
    
    def rem_fields(self,role,name,field):
        if role=="dean":
            for i in self.lst:
                if i.name==name:
                    i.category.remove(field)
        else:
            raise ValueError("You role can't remove fields!")
    
    def display(self):
        print("Here are all the records of people in this college:")
        for i in self.lst:
            print(i)
    
#Factory
class Member:
    def __init__(self,name : str,age : int,category = str):
        self.name=name
        self.age=age
        self.category=category.split(",")

class Student(Member):
    def __init__(self,name,age,category,dept):
        super().__init__(name,age,category)
        self.dept=dept
        self.role= "Student"
    def __str__(self):
        return f"""Name: {self.name}
        Dept: {self.dept}
        Age: {self.age}
        Role: {self.role}
        Field Of Interest: {str(self.category)[1:-1]}
        ---------------------------------------------
        """
    def getdict(self):
        d={"Name": self.name,
        "Dept": self.dept,
        "Age": self.age,
        "Role": self.role,
        "Field Of Interest": self.category}
        return d
class Faculty(Member):
    def __init__(self,name,age,category,dept,salary,role="Faculty"):
        super().__init__(name,age,category)
        self.dept=dept
        self.role=role
        self.salary=salary
       
    def __str__(self):
            return f"""Name: {self.name}
            Age: {self.age}
            Dept: {self.dept}
            Role: {self.role}
            Category: {str(self.category)[1:-1]}
            Salary: {self.salary}
            ---------------------------------------------
            """
    def getdict(self):
        d={"Name": self.name,
        "Dept": self.dept,
        "Age": self.age,
        "Role": self.role,
        "Field Of Interest": self.category,
        "Salary": self.salary}
        return d

class Staff(Member):
    def __init__(self,name,age,category,salary):
        super().__init__(name,age,category)
        self.role="Staff"
        self.salary=salary
        #since python already works with UTF-8, we don't have to explicity define anything to work with regional languages
    def __str__(self):
            return f"""Name: {self.name}
            Age: {self.age}
            Role: {self.role}
            Category: {str(self.category)[1:-1]}
            Salary: {self.salary}
            ---------------------------------------------
            """
    def getdict(self):
        d={"Name": self.name,
        "Age": self.age,
        "Role": self.role,
        "Field Of Interest": self.category,
        "Salary": self.salary}
        return d
        
#Abstract Factory
class Entity:
    @staticmethod
    def _(role,name,age,category,dept :str =None,salary :int =None):
        if role == "Student":
            return Student(name,age,category,dept)
        elif role == "Staff":
            return Staff(name,age,category,salary)
        else:
            return Faculty(name,age,category,dept,salary,role)


pplasn=PplAsn()
s1=Entity._("Student","Vishnu Siddharth",19,"ML,AI","IT")
s2=Entity._("Student","Vishal Prakash",20,"CyberSecurity,ML","ECE")
s3=Entity._("Student","Ravi Teja",19,"Ethical Hacking","IT")
s4=Entity._("Student","Mariappan",19,"ML,AI,DS","IT")
f1=Entity._("Faculty","Joesph",40,"ML,AI","ECE",100000)
f2=Entity._("Faculty","Chandru",42,"Ethical Hacking,Cyber Security","IT",120000)
f3=Entity._("Faculty","Kavya",35,"DS,AI","IT",100000)
st1=Entity._(role="Staff",name="कुमार",age=56,category="Security",salary=25000)
st2=Entity._(role="Staff",name="மாரியப்பன்",age=60,category="Security",salary=25000)

#appending
pplasn.append(s1)
pplasn.append(s2)
pplasn.append(s3)
pplasn.append(s4)
pplasn.append(f1)
pplasn.append(f2)
pplasn.append(f3)
pplasn.append(st1)
pplasn.append(st2)

#searching
print("Searching All Security")
pplasn.search("c","Security")

#updating salaries
pplasn.update_salary("Security",2000)

print("After salary update: \n ")
#demonstrating update
pplasn.search("c","Security")

#demonstrating adding fields
print("Adding Fields:")
hod=Entity._("HOD","Ada Williams",50,"AI,ML","IT",200000)
print("Before: ")
#before
pplasn.name_search("Vishnu Siddharth")

#adding
pplasn.add_fields(hod.role,"Vishnu Siddharth","Cyber Security")
print("After:")
#after
pplasn.name_search("Vishnu Siddharth")

#demonstrating removing fields
print("Removing Fields")
dean=Entity._("dean","Donuth",65,"AI,DS","ECE",250000)
print("Before: ")
#before
pplasn.name_search("Vishal Prakash")

#removing
pplasn.rem_fields(dean.role,"Vishal Prakash","CyberSecurity")
print("After:")
#after
pplasn.name_search("Vishal Prakash")


#displaying all the data
pplasn.display()

#pickling and depicking
import pickle
pl=[]
for i in pplasn.lst:
    pl.append(i.getdict())

with open ("data","wb") as file:
    for i in pl:
        pickle.dump(i,file)

print("All data successfully pickled")
print("-------------------")
print("Unpickling the data...")
#depickling
with open ("data",'rb') as file:
    while True:
        try:
            dat=pickle.load(file)
            print(dat)
            print()
        except EOFError:
            print("End Of File")
            break
#Vishal Prakash
#version1
#error found
#modified at 12-10 18:00 PM
#found not working at 12-10 22:00 pm

class Book:
    def __init__(self,data,subject,title,author,DDS,ISBN):
        self.data=data
        self.subject=subject
        self.title=title
        self.author=author
        self.DDS=DDS
        self.ISBN=ISBN
        self.data.append(self.subject)
        self.data.append(self.title)
        self.data.append(self.author)
        self.data.append(self.DDS)
        self.data.append(self.ISBN)
    def return1(self):
        return self.data
            
class DVD:
    def __init__(self,data,UPC):
        self.data=data
        self.UPC=UPC
        self.data.append(self.UPC)
class CD:
    def __init__(self,data,UPC):
        self.data=data
        self.UPC=UPC
        self.data.append(self.UPC)
        
class Magazine:
    def __init__(self,data,title,volume,issue):
        self.data=data
        self.title=title
        self.volume=volume
        self.issue=issue
        self.data.append(self.title)
        self.data.append(self.volume)
        self.data.append(self.issue)   
        
        
class Library:
    def __init__(self):
        
        D={'Books':[],'CD':[],'Magazines':[],'DVD':[]}
        self.D=D
        
    def AddBook(self):
        subject=input('enter the subject')
        title=input('enter the title')
        author=input('enter the author')
        ISBN=int(input('enter the ISBN number'))
        DDS=int(input('enter the DDS number'))
        B=Book([],subject,title,author,DDS,ISBN)
        b=B.return1()
        self.D['Books'].append(b)
    def AddDVD(self):
        UPC=int(input('enter the UPC number'))
        D=DVD([],UPC)
        self.D['DVD'].append(D)
    def AddCD(self):
        UPC=int(input('enter the UPC number'))
        C=CD([],UPC)
        self.D['CD'].append(C)
    def AddMag(self):
        title=input('Enter the title')
        issue=input('enter the issue')
        volume=int(input('enter the volume'))
        M=Magazine([],title,issue,volume)
        self.D['Magazines'].append(M)
    def return2(self):
        return self.D
        
        

def Add(ch):
    L=Library()
    if ch==1:
        L.AddBook()
    elif ch==2:
        L.AddCD()
    elif ch==3:
        L.AddDVD()
    elif ch==4:
        L.AddMag()
    else:
        print('Invalid Choice')

def Search():
    L=Library()
    l=L.return2()
    x=input('enter choice')
    if x==1:
        a=input('Enter the subject')
        b=input('enter the title')
        c=input('enter the author')
        d=int(input('enter the isbn number'))
        e=input('enter the dds number')
        
        for i in l['Books']:
            if i[0]==a and i[1]==b and i[2]==c and i[3]==d and i[4]==e:
                print('The book is found')
    elif x==2:
        a=int(input('enter the upc number'))
        for i in l['DVD']:
            if i[0]==a:
                print('Found')
    elif x==3:
        a=int(input('enter the upc number'))
        for i in l['CD']:
            if i[0]==a:
                print('Found')
    elif x==4:
        a=input('enter title')
        b=input('enter volume')
        c=input('enter issue')
        for i in l['Magazines']:
            if i[0]==a and i[1]==b and i[2]==c:
                print('Found')

def display():
    L=Library()
    for i in L.D.keys():
        print(i,L.D[i])
        print()
    print()


v='yes'
while v=='yes':
    print('''
    1- Add
    2- Search
    3- Display''')
    
    CH=int(input('enter choice: '))
    if CH==1:
        print('''
        1-Book
        2-CD
        3-DVD
        4-Magazine''')
        ch=int(input('enter choice2'))
        Add(ch)
    elif CH==2:
        Search()
    elif CH==3:
        display()
    else:
        print('invalid choice')
    
    v=input('Do you want to continue? ')


        


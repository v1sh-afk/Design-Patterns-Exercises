from ex02 import Point, Point2D, Point3D
#Vishal Prakash 
print('EXERCISE 02-VISHAL PRAKASH IT-B')        
P=Point()
x=int(input('Enter X coord: '))
y=int(input('Enter Y coord: '))
z=int(input('Enter Z coord: '))
X=int(input('Enter X coord: '))
Y=int(input('Enter Y coord: '))
Z=int(input('Enter Z coord: '))
if z==0:
    P1=Point2D(x,y)
else:
    
    P1=Point3D(x,y,z)
if Z==0:
    P2=Point2D(X,Y)
else:
    P2=Point3D(X,Y,Z)
x='yes'
while x=='yes':
    P=Point()
    print('''
        1-Distance
        2-Reset
        3-Convert
        4-Display''')
    ch=int(input('Enter your choice: '))
    
    
    if ch==1:
        print('DISTANCE')
        
        print(P.Distance(P1.getpoint(),P2.getpoint()))
    elif ch==2:
        print('RESET')
        print('''
            1-P1
            2-P2''')
        C=int(input('Enter the Point to be reset: '))
        if C==1:
            P1=P.Reset()
        elif C==2:
            P2=P.Reset()
        else:
            print('INVALID CHOICE')
    elif ch==3:
        print('CONVERT')
        print('''
            1-P1
            2-P2''')
        chh=int(input('Enter the point to be converted: '))
        if chh==1:
            P1=P.Convert(P1.getpoint())
            print(P1)
        elif chh==2:
            P2=P.Convert(P2.getpoint())
            print(P2)
        else:
            print('INVALID CHOICE')  
    elif ch==4:
        print('DISPLAY')
        print(P1.showpoint(),P2.showpoint())
    else:
        print('INVALID CHOICE')
    x=input('Do you want to continue?(yes/no) ')

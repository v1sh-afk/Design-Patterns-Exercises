import math
#P1=(x1,y1,z1)
#P2=(x2,y2,z2)
#Author-Vishal PRakash
#IT-B
class Point:
    def Distance(self,p1,p2):
        A=math.pow((p2[0]-p1[0]),2)
        B=math.pow((p2[1]-p1[1]),2)
        C=math.pow((p2[2]-p1[2]),2)
        
        return(math.sqrt(A+B+C))
    
    def Reset(self):
        P=Point3D(0,0,0)
        return P
    
    def Convert(self,P1):
        if len(P1)==2:
            return('The point is already in 2D')
        else:
            X=(P1[0]/P1[2])
            Y=(P1[1]/P1[2])
            return(Point2D(X,Y))  
           

class Point2D:
    def __init__(self,xcod,ycod):
        self.xcod=xcod
        self.ycod=ycod
        self.zcod=0
        
    def getpoint(self):
        return (self.xcod,self.ycod)
        
    def showpoint(self):
        print("x coordinate is:",self.xcod)
        print("y coordinate is:",self.ycod)
        
class Point3D:
    def __init__(self,xcod,ycod,zcod):
        self.xcod=xcod
        self.ycod=ycod
        self.zcod=zcod
        
    def getpoint(self):
        return (self.xcod,self.ycod,self.zcod)
        
    def showpoint(self):
        print("x coordinate is:",self.xcod)
        print("y coordinate is:",self.ycod)
        print("z coordinate is:",self.zcod)
        
        
if __name__=='__main__':
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
            
    print('THANK YOU')


    
        
        
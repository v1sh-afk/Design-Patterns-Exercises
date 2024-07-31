#Exercise6
#Vishal Prakash ITB


print('Create a string made of the first, middle and last character')
x=input('Enter the string: ')
x1=x[0]+x[len(x)//2]+x[-1]
print(x1)

print()

print('Create a string made of the middle three characters')
x=input('Enter the string: ')
mid=len(x)//2
x2=x[mid-1]+x[mid]+x[mid+1]
print(x2)

print()

print('Append new string in the middle of a given string')
x=input('Enter the given string: ')
mid=len(x)//2
X=input('Enter the new string: ')
x3=x[:mid]+X+x[mid:]
print(x3)

print()

print('Create a new string made of the first, middle, and last characters of each input string')
x4= x1+X[0]+X[len(X)//2]+X[-1]
print(x4)
print()

print('Arrange string characters such that lowercase letters should come first')
x=input('Enter the string: ')
r1=''
r2=''
for i in x:
    if i.islower():
        r1+=i
    else:
        r2+=i
r=r1+r2
print(r)

print()

print('Count all letters, digits, and special symbols from a given string')
x=input('Enter the given string: ')
c1=0
c2=0
c3=0

for i in x:
    if i.isalpha():
        c1+=1
    elif i.isdigit():
        c2+=1
    else:
        c3+=1
print('The number of letters in the string is,', c1)
print('The number of digits in the string is,', c2)
print('The number of special symbols in the string is,', c3)

print()

print('''
String characters balance Test: For example, strings s1 and s2 are balanced
if all the characters in the s1 are present in s2. The character’s position
doesn’t matter''')

s1=input('Enter String s1: ')
s2=input('Enter string s2: ')
L1=[]
L2=[]
for i in s1:
    L1.append(i)

for j in s2:
    if j!=' ':

        L2.append(j)

L1.sort()
L2.sort()

if len(L1)>len(L2):
    print('Not Balanceed')
else:
    L2=L2[:len(L1)]
    if L1==L2:
        print('Balanced')


print()

print('Find all occurrences of a substring in a given string by ignoring the case')
x=input('Enter the given string: ')
x5=input('Input the substring: ')
L3=x.split()
c4=0
for i in L3:
    if i.lower()==x5.lower():
        c4+=1

print(f'The number of occurrences of {x5} in the string {x} is,', c4)
print()


print('Calculate the sum and average of the digits present in a string')
x=input('Enter the given string: ')
L4=[]
c5=0
c6=0
for i in x:
    if i.isdigit():
        L4.append(i)
for i in L4:
    c5+=int(i)
c6=c5/len(L4)

print('Sum',c5)
print('Average',c6)

print()

print('Find the last position of a given substring')
x=input('Enter the given string: ')
x6=input('Enter the substring: ')

X=x[::-1]
Y=x6[::-1]
Z=X.partition(Y)
c=0
for i in range(2):
    c+=len(Z[i])

print('The last position of a given substring is,', len(x)-c+1)

print()

print('Split a string on hyphens')
x=input('Enter the given string: ')
print(x.split('-'))

print()

print('Remove empty strings from a list of strings')
x=input('Enter the given string: ')
r3=''
for i in x:
    if i!=' ':
        r3+=i

print(r3)

print()

print('Remove special symbols /, punctuation from a string and replace each special symbol with # in the string')
x=input('Enter the given string: ')
r4=''
for i in x:
    if i in '\'"/,':
        r4+='#'
    else:
        r4+=i
print(r4)

print()


print('Removal all characters from a string except integers')
x=input('Enter the given string: ')
r5=''
for i in x:
    if i.isdigit():
        r5+=i

print(r5)
print()


print('Find words with both alphabets and numbers')
x=input('Enter the given string: ')
L6=x.split()
for i in L6:
    c=0
    for j in i:
        if j.isdigit():
            c+=1
        if j.isalpha():
            c+=2
    if c>=2:
        print(i)

print()
print('The end')



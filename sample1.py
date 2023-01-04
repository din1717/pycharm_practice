"""
import random
a= [1,3,5,1,8,1,2,9,2,3,2,4,1,4,5,4,6,7,6,3,6]
def matrix():
    samplepoutput = []
    for i in range(a):
        if a==i:
            samplepoutput.append()
            return samplepoutput

matrix()
import sys
sys.exit(0)
1.
Form a 3 * 3 matrix by choosing randomly from the below list
a = [1, 3, 5, 1, 8, 1, 2, 9, 2, 3, 2, 4, 1, 4, 5, 4, 6, 7, 6, 3, 6]
Sample Output: [[1, 4, 5], [3, 9, 8], [2, 3, 5]]
Wrong output: [[1, 4, 4], [3, 9, 8], [2, 3, 5]]
Rules: Same number should not be repeated again in a row

#maximum of two numbers

a = 2
b = 4
def maximum():
    if a>b:
        print(a)
    else:
        print(b)
maximum()

l = [10, 20, 30, 40]

prime = []

for i in l:
    if (l%i)==0
count = 1
a = [1,2,34,5,6]
b = []
for i in a:
    if i==35 or i<=35:
        b.append(i)
        print(b)

lis=[1,4,10,12,11,31,77,67]
prime=[]
for i in lis:
c=0
for j in range(1,i):
if i%j==0:
c+=1
if c==1:
prime.append(i)
print(prime)
output: [11,31,67]

lis=[1,4,10,12,11,31,77,67]
l = []

for i in lis:
    if (i%2)==1 and i>0:
        l.append(i)
print(l)

# test_list = [(1, 'abc', 'Hyderabad'), (2, 'xyz', 'Bangalore')]

# Write python code to convert above list into a string as below.

# Result: "(1, 'abc', 'Hyderabad'), (2, 'xyz', 'Bangalore')"
a = [(1, 'abc', 'Hyderabad'), (2, 'xyz', 'Bangalore')]
print('original list : '+ str(a))
result = str(a).strip("[]")
print(result)
print('"',result,'"')
#print(' :'+ "str(result)")
#print('Final list :',end="result")
print(result)

mystr = "mahesh is a clear boy"
print(mystr.center(5))

mystr.strip()
mystr.join()
mystr.split()
mystr.format()
mystr.count()
mystr.index()
mystr.capitalize() # first string letter convert into capital
mystr.casefold() # all letter converted into small letter
mystr.center()
mystr.encode()
mystr.endswith() # print last word from string
mystr.expandtabs()
mystr.find() # give any word then he give postion of that word
mystr.format_map()
mystr.isalnum()
mystr.isascii()
mystr.isdecimal()
mystr.isalpha()
mystr.isidentifier()
mystr.isdigit()
mystr.zfill()
mystr.translate()
mystr.title()
mystr.istitle()
mystr.format()
mystr.isprintable()
mystr.swapcase()


print("The original list is : " + str(test_list))

# List of tuples to String
# using str() + strip()
res = str(test_list).strip('[]')

# printing result
print("Resultant string from list of tuple : " + res)

all prime number form list

a = [1,23,4,56,78,2,3,4]

def prime(

l = []
def fun(list):
    sum = 0
    for i in list:
        if i==1:

            l.append(i)
            sum= sum+ 1
        return sum


fun(list)
print(l)
def swaplist(newlist):
    size = len(newlist)

    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1]= temp
    return newlist


newlist = [12, 35, 9, 56, 24]
print(swaplist(newlist))
#print(a)

#1)
#b = [1,1,2,2,2,2,3,4,4,4,4]
import operator
a = {1:12,2:21,3:42,4:5}
d = sorted(a.items(),key=operator.itemgetter(1))
e = sorted(a.items(),reverse=True)
f = sorted(a.keys())
print('ascending :',d)
print('Descending :',e)
print(f)
2)
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
a = {0:10,1:20}
b = {2:30}
or a.update({2:30})
a.update(b)
print(a)
3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
1 method
a={1:10, 2:20}
b={3:30, 4:40}
c={5:50,6:60}
a.update(b)
print(a)
a.update(c)
print(a)
2 method
a={1:10, 2:20}
b={3:30, 4:40}
c={5:50, 6:60}
d = {}
for i in a,b,c:d.update(i)
print(d)


a={1:10, 2:20}
def abs(c):
    if c in a:
        print(True)
    else:
        print(False)
abs(3)

date - 30/09/2022
1) Given two numbers num1 and num2. The task is to write a Python program to find the addition of these two numbers. Examples:

a = int(input('Enter the a :'))
b = int(input('Enter the b :'))

def addition(a,b):

    if a and b:
        print('Addition :', a+b)
    else:
        print('No proper no are there ')
def substraction(a,b):
    if a and b:
        print('substraction :', a-b)
    else:
        print('No proper no are there ')

addition(a,b)
substraction(a,b)
2)get maxmium from two number
method 1
for i in range(5):
    a = int(input('Enter the a :'))
    b = int(input('Enter the b :'))
    if a > b:
        print('max :', a)
    else:
        print('min : b')
method 2
a = 12
b = 13

max1 = max(a,b)
print(max1)

method 3 Using Ternary Operator
a = 12
b = 16
print(a if a>=b else b)
 method 4
using lambda function
a = 12
b = 16
max1 = lambda a,b : a if a>=b else b
print(f'{max1(a,b)} is a maxmium number')



def factorial(n):
    if n:
        print('a :',n * factorial(n-1))
3)
simple interest formula is given by: Simple Interest = (P x T x R)/100
Where, P is the principle amount T is the time and R is the rate
p = int(input('Enter the p : '))
t = int(input('Enter the t : '))
r = int(input('Enter the r : '))
def simple_interest(p,t,r):
    if p and t and r:
        si = (p * t * r) / 100
        print('Ans : ',si)
    else:
        print('No match')
simple_interest(12,12,12)

4)compund interest
p = int(input('Enter the p : '))
t = int(input('Enter the t : '))
R = int(input('Enter the r : '))
def compund_interest(p,t,r):
    if p and t and r:
        A = p*(1 + R/100)**t
        print('Ans : ',A)
    else:
        print('No match')
compund_interest(12,12,12)

5)area of circle
#Area = pi * r2
r = int(input('Enter the r : '))
pr = 3.14
def area_of_circel(r):
    if r:
        area = pr*(r*r)
        print('ad :',area )
    else:
        print('No')
area_of_circel(r)
date 2/10/22
#5! = 5*4*3*2*1 (n*(n*(n-1)))
1)
method 2
def factorial(n):
    if n:
        a = n*(n-1)*(n-2)*(n-3)*(n-4)
        print(a)
#factorial(6)
method 2
def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1);
num = 6;
print("factorail of",num,"is",factorial(num))

#2)list negative

a = [1,23,32,12,14]

b = sorted(a,reverse=True)
print(b)
print('slicing',b[::-1])
l = []
for i in b:
    l.insert(0,i)
print(l)

Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

a = 153
b = str(a)
print(len(b))
c = b[0]*len(b) + b[1]**len(b) + b[2]*len(b)
d =  len(b)*b[1]
print(d)
if a==c:
    print('Armsstrong')
else:
    print('not')
3)
#prime = 2,3,5,7,11
l = []
def prime_number():
    for i in range(0,10):
        print('list',i)
        if i % 2 == 1:
            l.append(i)
            return l
        else:
            print('no')
prime_number()
a = []
def avcd():
    for i in range(0,10):
        if i%2==1:
            a.append(i)
    print(a)
avcd()
4)
a=1
if a%2==1:
    print('prime')
else:
    print('no')

a = 98
c = chr(a)
print(c)

d = 'a'
g = ord(d)
print(g)
5)
Input : N = 4
Output : 30
12 + 22 + 32 + 42
= 1 + 4 + 9 + 16
= 30

n=5
c=  (n-4)*(n-4)*(n-4) + (n-3)*(n-3)*(n-3) + (n-2)*(n-2)*(n-2) + (n-1)*(n-1)*(n-1) + (n)*(n)*(n)
print(c)

Input : arr[] = {1, 2, 3}
Output : 6
1 + 2 + 3 = 6


Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]



def swap(a):
    a[0],a[4]=a[4],a[0]
    return a
a = [12, 35, 9, 56, 24]
print(swap(a))

from collections import Counter
a=[]
b = []
list = [1,1,2,2,2,3,3,4,4,5]
for i in list:
    if i not in a:
        a.append(i)
for i in a:
    count = 0
    if i in a:
        #b.append(i)
        count = count + 1
print(count)

#print(a)

list = [1,1,2,2,2,3,3,4,4,5]
counts = {}
for n in list:
    counts[n] = counts.get(n,0) + 1
print(counts)

for i in counts:
    if i==1:
        print(i)

test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}

list = []
def dict(test_dict):
    for i in test_dict:
        if i not in list:
            list.append(i)
            print(list)


dict(test_dict)

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2
for i in range(4):
    print("please select operators \n"
          "1.add\n"\
        "2.sub\n"\
        "3.mul\n"\
        "4.div\n")

    select = int(input("Select operations form 1,2,3,4 : "))

    number_1 = int(input("Enter the number : "))
    number_2 = int(input("Enter the number : "))

    if select==1:
        print(number_1,"+",number_2,"=",add(number_1,number_2))
    elif select==2:
        print(number_1,"-",number_2,"=",sub(number_1,number_2))
    elif select==3:
        print(number_1,"*",number_2,"=",mul(number_1,number_2))
    elif select==4:
        print(number_1,"/",number_2,"=",div(number_1,number_2))
    else:
        print("Invalid Input")
#interchange element
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

def swap(i):
    i[0],i[4]=i[4],i[0]
    return i


i=[12, 35, 9, 56, 24]
print(swap(i))


def swap(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0,last)
    list.append(first)
    return list
list = [12,123,14,14,13]
print(list)
print(swap(list))
#swap element
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

def swap(list):
    list[2],list[0]=list[0],list[2]
    return list
list = [23,65,19,90]
print(swap(list))

def swap(list):
    first = list.pop(2)
    last = list.pop(0)

    list.insert(0,last)
    list.insert(2,first)
    return list
list= [23,65,19,90]
print(swap(list))


list = [1, 6, 3, 5, 3, 4]

i = 7
if i == 3:
    print("True")
else:
    print("False")
#check elemetn exits

list =  [1, 6, 3, 5, 3, 4]
for i in list:
    if i==4:g
        print("element exits")

list  = [1,2,3,4]
a = [i for i in list if i==4 ]
print(a)
various method to clear the list

list  = [1,2,3,4]
print("before",list)
list.clear()
print("after",list)

list  = [1,2,3,4]
del list[:]
print("after1",list)

list = [1,2,3,4]

list.reverse()
print("af",list)
print(list[::-1])

a = 123%10
print(a)
import sys
sys.exit(0)
list = 1234
reversed_list = 0
while list !=0:
    digit = list%10
    print(digit)
reversing the number
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    print('as',reversed_num)

    num //= 10
    print(num)


print("Reversed Number: " + str(reversed_num))
method2
num1 = 1234
print("After",str(num1)[::-1])

a = "abcd"
print(str(a)[::-1])

#Input: [12, 15, 3, 10]
#Output: 40
#d = []
#a = [12,15,3,10]


def sum(a):
    num = 0
    for i in a:
        num = num + i
    return num
a = [12,15,3,10]
print(sum(a))

Input :  list1 = [1, 2, 3]
Output : 6
Explanation: 1*2*3=6

def mul(a):
    num = 1
    for i in a:
        num = num*i
    return num
a = 1,2,3
print(mul(a))

Input : list1 = [10, 20, 4]
Output : 4

a = [12,13,14,15,21,2,1.5,34,7]
a.sort()
print(a[0])
#print(a)

a = [12,13,14,15,21,2,1.5,34,7]
#a.sort()
for i in range(len(a)):
    #print("i format",i)
    for j in range(i+1,len(a)):
        #print("j format",j)`

        if a[i]>a[j]:

            print('a',a[i])
            print('b',a[j])
            #print("jsass", j)
            a[i],a[j]=a[j],a[i]
print(a)



n = []
def sort(a):
    num = 0
    for i in a:

        #num = num + i
        if num>i:
            n.append(num)
            return n

a = [12,13,14,15,21,2,1.5,34,7]
print(sort(a))

#sort the list without built in function


a = [12,13,14,15,21,2,1.5,34,7]
b = []
while a:
    min = a[0]
    #print(min)
    for x in a:
        if x < min:  #12 highest aahe tr mg 12 che pahile sagle number add honar aane remove pn honar
            min = x
    b.append(min)
    a.remove(min)
print(b)

import sys
sys.exit(0)

#Highest number
a = [12,13,14,15,21,2,1.5,34,7]
a.sort()
print(a[-1])

#Input: list2 = [70, 11, 20, 4, 100]
#Output: 70

a = [0, 11, 20, 4, 100]
a.sort()
print(a)
print(a[-2])


a = [0, 11, 20, 4, 100]
for i in range(len(a)):
    print((i))
    for j in range(i+1,len(a)):
        print(j)
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)
    #print(i)

a = [0, 11, 20, 4, 100]
if a[i] > a[j]:
    a[i], a[j] = a[j], a[i]
print(a)

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

def ot():
    def it():
        for ot in range(5):
            for it in range(5):
                print(ot,it,end='\t\t')
            print('\n')
    it()
ot()
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

row  = 5
for i in range(1,row+1,1):

    for j in range(1,i+1):
        print(j,end=' ')
    print("")

#For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

def inner(n):
    sum = 0
    for i in range(1,n+1,1):
        sum = sum + i

    #1717


    print(sum)
n = int(input('Enter the number :'))
inner(n)

s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)

nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']

pos = nameList.index("GeeksforGeeks")


print(pos * 3)

D = dict()
for x in enumerate(range(2)):
	D[x[0]] = x[1]
	D[x[1]+7] = x[0]
print(D)

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

# 2
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)

a = [1,2,3,4]
#a.pop()
print(a.pop())

a ={1,2,3,4,8,10}
a.add(9)
print(type(a))
print(a.add(11))

# Python code to demonstrate addition of tuple to a set.
s = {'g', 'e', 'e', 'k', 's'}
t = ('f', 'o')
l = ['a', 'e']

# adding tuple t to set s.
s.add(t)

# adding list l to set s.
s.update(l)
print(s)

def swaplist(a):
    a[1],a[-2] = a[-2],a[1]
    return a

a = [1,2,3,4]
print(swaplist(a))

def swap(test_list):
    test_list[0],test_list[-1] = test_list[-1],test_list[0]
    return test_list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
print(swap(test_list))

replace words from string
a = ['Gfg', 'is', 'best', 'for', 'Geeks']
c = [i.replace('G','-').replace('e','G').replace('-','e') for i in a]
print(c)

a = ['Gfg', 'is', 'best', 'for', 'Geeks']
c = ", ".join(a)
d = [c.replace('G','-').replace('e','G')]
print(c)

def len(a):
    count = 0
    for i in a:
        count = count + 1
    print(count)
a = [1,2,3,4,76.10,78,4]
len(a)

a = [1,2,3,478,90,5,8,12]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        #print(j)
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a)
b = a[-1],a[-2]
print(b)

a =  ['abcd','ab1','ab3']
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a)

a =  2
b = 3
if a<b:
    print(a)
else:
    print(b)

reversing the list
a = [1,2,3,4,5]
print(a[::-1])

a.reverse()
print('after',a)

for i in range(len(a)):
    for j in range(len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print('sort',a)

#list slicing, extend ,shallow copy,deep copy,copy,append,list compresion,assignment operator

def cloning(a):
    b = a[:]
    return b
a = [1,2,3,4]
print('list_slicing :-',cloning(a))

def cloning(a):
    b = []
    b.extend(a)
    return b
a = [1,2,3,4]
print('extend :-',cloning(a))

import copy
def cloning(a):
    b = copy.copy(a)
    return b
a = [1,2,3,4]
print('shallow copy',cloning(a))

def cloning(a):
    b = copy.deepcopy(a)
    return b
a = [1,2,3,4]
print('deep copy',cloning(a))

def cloning(a):
    b = []
    for i in a:b.append(i)
    return b
a = [1,2,3,4]
print('append :-',cloning(a))

def cloning(a):
    d = [i for i in a]
    return d
a = [1,2,3,4]
print('list com',cloning(a))

def cloning(a):
    b = a
    return b
a = [1,2,3,4]
print('assignment operator :', cloning(a))

a = [1,2,1,1,2,3,4]
#print(a.count(1))

b = []
def cal(a):
    count = 0
    for i in a:
        if i==b:
            count = count + 1
        else:
            b.append(i)

    print()
a = [1,2,1,1,2,3,4]
print('asd',cal(a))
#print(f"{key:values}")

x = 3
#d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))

a = [1,1,1,1,2,2,3,4,4,5,5,5,5]
c = []
b = []
for i in a:
    if i not in c:
        c.append(i)
    else:
        b.append(i)

print(c)
print(b)

a = 'aaaabbbccz'
a[0] ='i'
c = 0
for i in a:
    if i==p:
        c = c+1
print(c)

Input : [4, 5, 1, 2, 9]
        N = 2
Output :  [9, 5]


def asd(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a

a = [4, 5, 1, 2, 9]
#asd(a)
print(asd(a))
b = a[0:2]
print(b)

a = [i if i%2==0 else i+1 for i in range(10) ]
print(a)

def asf(a):
    for i in a:
        if i>=0:
          print(i,end=',')
a = [12,2,3,-2,-4]
asf(a)

Input: [12, 15, 3, 10]
Output: Remove = [12, 3], New_List = [15, 10]

Input: [11, 5, 17, 18, 23, 50]
Output: Remove = [1:5], New_list = [11, 50]

b = [12, 15, 3, 10,11,43,13]

umwanted = [0,2,3]
for i in sorted(umwanted,reverse=True):
    del b[i]
print(b)

a = [1,2,3,[],4,5,[],6,7]
for i in a:
    if i!=[]:
        print(i,end=',')


b = []
def asd(tuples):
    for i in tuples:
        if i!=() and i!=('',''):
            b.append(i)
    #print(b)
    return b
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
                  ('krishna', 'akbar', '45'), ('',''),()]
asd(tuples)
print(b)
d = str(b)
print(d)
            #print(i,end=',')



if ((5!=5) and (5>3)):
    print("1")

elif ((5!=5) or (5<3)):
    print("2")

elif ((5!=5) or (3>5)):
    print("3")

elif((5!=5) or (5>3)):
    print("4")

elif((5<=3) or (5>=3)):
    print("5")

elif((5>3) and (5<10)):
    print("6")

else:
    print("7")

x = 1

y = 1

x = y = y + 3;x = x + (True)

print(x)




y = 12L

z = 12

v = y + z

print(v)

s = {'e':4,'f':5}
print(s.get('f'))


#How do you extract the value for key f?

x = 'y'

z = { x: 'junk' }
print(z[0])

def hose():

  try:

    1/1

    return 22

    return 23

  finally:

    return 24



hose()

def goat():

  try:

    1/0

    return 23

  finally:

    return 24



goat()

c = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
print(c)

d = dict([('y', 2), ('x', 1), ('z', 3)])
print(d)
e = dict({'z': 3, 'x': 1, 'y': 2})
print(e)
b = {'x': 1, 'y': 2, 'z': 3}
print(b)
a = dict(x=1, y=2, z=3)
print(a)

Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]

a = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
b = []
c = []
for i in a:
    if i in b:
        b.remove(i)
    else:
        b.append(i)
for i in c:

print(b)

def str(string):
    count = {}
    for i in string:

        if i in count:
            count[i] +=1
        else:
            count[i] = 1

    return count
string = "google.com"
print(str(string))
Write a Python program to count the number of characters (character frequency) in a string.
def char(a):
    d = {}
    for i in a:
        if i in d:
            d[i] +=1
        else:
            d[i] = 1
    return d
a = "google.com"
print(char(a))

Write a Python program to get a string made of the first 2 and
the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
def slice(a):
    l = len(a)
    for i in range(0,len(a)):
        #print(i)
        if l==1:
            print('len is less')
            break
        elif l>=3:
            new = a[0:2] + a[-2:]
            return new
        elif l<=2 and l>=1:
            new = a[0:2] + a[0:2]
            return new
        else:
            continue
a = "og"
print(slice(a))

Write a Python program to get a string from a given string
where all occurrences of its first char have been changed to '$', except the first char itself.
def stri(a):
    d = a[0]
    a = a.replace(d,'$')
    a = d+a[1:]
    return a
print(stri('restart'))
def strig(a):
    e = a[0]

    for i in a:
        if i in a:
            a = a.replace(e,'$')
            a = e + a[1:]
    return a
a = 'restart'
print(strig(a))
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

a = 'abc'
b = 'xyz'
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]
c = a1 + ' ' + b1
c.strip(''.join(c))
print(type(c))
print(c)
Write a Python program to find common items from two lists.
c = []
def comman(a,b):
    for i in b:
        if i in a:
            c.append(i)
    return c
a = [1,2,3,4,6,7]
b = [2,3,4,5,6]
print(comman(a,b))

a = [1,2,3,4,6,7]
b = [2,3,4,5,6]
print(set(a) and set(b))

Write a Python program to change the position of every n-th value with the (n+1)th in a list.
Sample
list: [0, 1, 2, 3, 4, 5]
Expected Output: [1, 0, 3, 2, 5, 4]

def swap(a,pos1,pos2):
    a[pos1],a[pos2] = a[pos2],a[pos1]
    return a
a = [0, 1, 2, 3, 4, 5]
d = swap(a,0,1)
e = swap(a,2,3)
f = swap(a,4,5)
print(f)
#[1, 0, 3, 2, 5, 4]
Write a Python program to convert a list of multiple integers into a single integer.
a = [11,22,33]
b = str(a)
d = int("".join(b))
print(d)

def string(a):
    b = [str(i) for i in a]
    d = int("".join(b))
    return (d)

a = [11,22,33]
print(string(a))
# this is not working i don't know why but whenever you are using list compreshion then he worked
def string1(c):
    for i in c:
        d = str(i)
        e = int("".join(d))
        return e
c = [11,22,33]
print(string1(c))

obj = {}
for i in range(1,21):
    obj[str(i)] = []
print(obj)
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

def splitLst(x):
    dictionary = dict()
    for word in x:
       # print(word)
        f = word[0]
        #print(f)
        if f in dictionary.keys():
            #print('if',f)
            dictionary[f].append(word)
            #print(dictionary[f])
        else:
            dictionary[f] = [word]
            #print(dictionary[f])

    return dictionary

x = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
print(splitLst(x))

6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3,
leave it unchanged. Go to the editor
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'

#print(l)
def acs(a):
    l = len(a)
    for i in a:
        if l<2:
            return a
        elif a[-3:] == 'ing':
            return a+'ly'

        else:
            return a+'ing'
a = 'abc'
print(acs(a))

Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def acs(a):
    substing = 'not that poor'
    d = 'good'
    for i in a:
        if i == substing:
            return a.replace(substing,d)

a = 'The lyrics is not that poor!'
'The lyrics is poor!'
print(acs(a))

a = 'The lyrics is not that poor!'
'The lyrics is poor!'
substring = 'not'
e = 'good'
d = a.split()

#please solve after some time
if substring in d:
    #print('yes')
    print(a.replace(a[])


def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
        return str1
    else:
        return str1


print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))

#Write a Python function that takes a list of words and return the longest word and the length of the longest one.
def word_length(a):
    word_len = []
    for i in a:
        word_len.append((len(i),i))
    word_len.sort()

    return word_len[-1]

a = ['php','excersice','dinesh']
print(word_length(a))
z = [1,2,3,4]
a = 4
n = ''
for i in range(0,len(z)):
    if(i != a):

        n += str[i]
print(n)

a =20
b =50
c =b%a
print(c)
def solve(a, b):
   return b if a == 0 else solve(b % a, a)
print(solve(20, 50))

def solve(a):
   a = [1, 3, 5]
a = [2, 4, 6]
print(a)
solve(a)
#print(a)
def func():
    global value
    value = "Local"
value = "Global"
func()
print(value)

a = [1,2]
print(a*3)
tuple return list after sort
numbers = (4, 7, 19, 2, 89, 45, 72, 22)
print(type(numbers))
sorted_numbers = sorted(numbers)
print(sorted_numbers)

#filter return object of filter not list
numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
even = lambda a: a % 2 == 0
even_numbers = filter(even, sorted_numbers)
print(type(even_numbers))

word = "Python Programming"
n = len(word)
word1 = word.upper()
word2 = word.lower()
converted_word = ""
for i in range(n):
    print(i)
    if i % 2 == 0:
        converted_word += word2[i]
    else:
        converted_word += word1[i]
print(converted_word)

print(type(type(int)))
a = [12,23,4,5]
a.pop(1)
print(a)

a = {1,2,3}
b = {4,5,6}
c = a + b
print(c)

s1 = {1, 2, 3, 4, 5}
s2 = {2, 4, 6}
print(s1 ^ s2)
"""
a = [[], "abc", [0], 1, 0]
print(list(filter(bool, a)))
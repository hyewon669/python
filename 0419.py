##i=int(input())
##if i >=90:
##     print("A")
##elif i <90 and i>=80:
##     print("B")
##else :
##     print("F")

##i=int(input())
##if i%2==0:
##     print("EVEN")
##else :
##     print("ODD")
##y=int(input('year : '))
##if (y%4==0 and y%100!=0) or y%400==0:
##     print('leap year')
##else:
##     print('common year')

##case = ['Homework' , 'Eating' , 'Sleeping']
##
##if 'Homework' in case :
##     print("I have to do homework.")
##else :
##     print("It's break time.")

##i=input() 
##if i=="M":
##     print("Man")
##elif i=="W":
##     print("Woman")
##else :
##     print("What")

##i=int(input())
##j=int(input())
##k=int(input())
##if i==j==k :
##     print(10000+i*1000)
##elif i==j!=k :
##     print(1000+i*100)
##elif i==k!=j : 
##     print(1000+i*100)
##elif j==k!=i :
##     print(1000+j*100)
##else:
##     
##     if i>j and i>k:
##          print(i*100)
##     elif j>i and j>k:
##          print(j*100)
##     else:
##          print(k*100)

from random import *

i=randint(0,1)
j=randint(0,1)
k=randint(0,1)
l=randint(0,1)
print( i , j, k, l)
if i+j+k+l==4:
     print("E")
elif i+j+k+l==0:
     print("D")
elif i+j+k+l==3:
     print("C")
elif i+j+k+l==2:
     print("B")
else :
     print("A")

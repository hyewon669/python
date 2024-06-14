##def waring():
##     for _ in range(3):
##          print("Fire!")
##waring()

##def two_times() :
##     for i in range(1,10):
##          print("2*%d = %d" %(i,2*i))
##two_times()

##def A() :
##     print(1)
##     r=B()
##     print(r)
##def B():
##     print(2)
##     return 3
##A()
##print(4)

##def f(n):
##     print(n)
##
##     if n > 1:
##          f(n-1)
##f(3)

##def factorial(n):
##     if n==1:
##          return 1
##     else :
##          return n * factorial(n-1)
##fac=factorial(4)
##print("4! =",fac)

##def judge(n) :
##     if n>0:
##          print("plus")
##     elif n<0:
##          print("minus")
##     else :
##          print("zero")
##n=int(input())
##judge(n)

##def season(month):
##     if month==3 or month==4 or month==5:
##          print("spring")
##     elif month==6 or month==7 or month==8:
##          print("summer")
##     elif month==9 or month==10 or month==11:
##          print("fall")
##     else:
##          print("winter")
##month=int(input())
##season(month)

##from random import*
##def lotto():
##     lot =set()
##     while len(lot)<6:
##          lot.add(randint(1,45))
##     lot=list(lot)
##     lot.sort()
##     print(lot)
##lotto()

##def times_table(a,b):
##     if a<b:
##          for i in range(a,b+1):
##               print("==%d Times=="%i)
##               for j in range(1,10):
##                    print("%d * %d= %d"%(i,j,i*j))
##     elif a>b:
##          for i in range(b,a+1):
##               print("==%d Times=="%i)
##               for j in range(1,10):
##                    print("%d * %d= %d"%(i,j,i*j))
##n=input().split()
##a=int(n[0])
##b=int(n[1])
##times_table(a,b)
##def func_abs(a):
##     if a>0:
##          print(a)
##     else:
##          print(a*-1)
##a=int(input())
##func_abs(a)
##def f(n):
##     for i in range(1,n+1):
##          k=0
##          for j in range(1,n+1):
##               k=k+i
##               print(k,end=" ")
##          print()
##n=int(input())
##f(n)

def point(n):
     print(n[1])
n=input().split('.')
point(n)

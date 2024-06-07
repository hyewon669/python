##def add(x,y):
##     s=x+y
##     return s
##result = add(10,20) + add(20,30)
##print(result)

##def get_max(x,y):
##     if x>y:
##          return x
##     else :
##          return y
##x=int(input())
##y=int(input())
##
##n=get_max(x,y)
##print(n)

##def plus(x):
##     if x>0:
##          print("Ture")
##     elif x<0:
##          print("Flase")
##
##x=int(input())
##n=plus(x)

##def get_sum(x,y):
##     s=0
##     for i in range(x,y+1) :
##          s += i
##     return s
##
##x = int(input())
##y=int(input())
##
##print("%d부터 %d까지의 합은 %d입니다."%(x,y,get_sum(x,y)))

##def area(x,y):
##     sum=x*y
##     return sum
##x=int(input())
##y=int(input())
##print(area(x,y))

##def number(n):
##     if n%2==0:
##          print("even")
##     else:
##          print("odd")
##n=int(input())
##number(n)

##def square(a,b):
##     sum=a**b
##     return sum
##a=int(input())
##b=int(input())
##print(square(a,b))

##def get_max(n):
##     s=0
##     for i in range(n):
##          n=int(input())
##          if n>s:
##             s=n
##     return s
##n=int(input("Enter integer n : "))
##print("max value :",get_max(n))

##def sum(a,b,c):
##     if b=='+' :
##          su=a+c
##     elif b=='-' :
##          su=a-c
##     elif b=='*' :
##          su=a*c
##     else :
##          su=a//c
##     return su
##
##
##n=input().split()
##n[0]=int(n[0])
##n[2]=int(n[2])
##print(sum(n[0],n[1],n[2]))

def login(id ,password):
     if id=='Cube' and password== '1234':
          result=1
     elif id=='Cube' and password != '1234':
          result=2
     elif id!='Cube' and password == '1234':
          result=3
     else:
          result=4
     return result
def say(result):
     if result==1:
          print("Login success")
     elif result==2:
          print("please check your PW")
     elif result==3:
          print("please check your ID")
     else:
          print("please check your ID and PW")

i=input("ID :")
p=input("PW:")
re=login(i,p)
res=say(re)

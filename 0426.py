##from random import *
##b=randint(0,6)
##
##a=['월','화','수','목','금','토','일']
##print(a[b])

##from random import *
##a = [1,2,3,4,5]
##print(choices(a ,[1,1,1000,1,1],k=1000))

##from random import *
##a=[0,1,2,3,4,5]
##b=choice(a)
##if b==0 :
##     print("Loss!")
##else :
##     print("No.%d Spot!"%b)

##from random import *
##import turtle
##house = turtle.Turtle()
##house.penup()
##house.goto(300,-250)
##house.fillcolor("saddlebrown")
##house.begin_fill()
##house.pendown()
##house.goto(400,-250)
##house.goto(400,-150)
##house.goto(300,-150)
##house.goto(300,-250)
##house.end_fill()
##house.fillcolor("burlywood")
##house.begin_fill()
##house.goto(300,-150)
##house.goto(350,-50)
##house.goto(400,-150)
##house.goto(300,-150)
##house.end_fill()
##line = turtle.Turtle()
##line.penup()
##line.goto(-300,-250)
##line.pendown()
##line.write("0")
##line.goto(0,-250)
##line.write("50")
##line.goto(300,-250)
##line.write("100")
##
##t=turtle.Turtle(shape = "turtle")
##t.penup()
##t.goto(-320,-250)
##t.color('turquoise')
##g=turtle.Turtle()
##g.write("씨큐브 코딩의 타자 게임!", True,font = ("Arial",20,"bold"))
##fruit=["apple","banana","strawberry","watermelon","mandarin","peach","grapes","orange","pear","kiwi"]
##score=0
##n=randint(5,10)
##for i in range(n):
##     s = choice(fruit)
##     word=turtle.textinput("fruit",'%s(%d/%d)'%(s,i+1,n))
##     if word==s:
##          score+=1
##
##rate=score / n*100
##g.penup()
##g.goto(0,-50)
##g.pendown()
##g.write("%d/%d번 성공!" %(score,n), True,font=("Arial",15,"bold"))
##g.penup()
##g.goto(0,-100)
##g.pendown()
##g.write("정확도 : %.1f%%" %(rate),True,font = ("Arial",15,"bold"))
##
##distance = t.distance(line)/100*rate
##t.speed(1)
##t.forward(distance)
##if rate==100:
##     t.write("집에 데려다줘서 고마워!! ♬",False,"center",font = ("Arial",15,"normal"))
##     t.left(60)
##     t.right(60)
##     t.left(60)
##     t.right(60)
##elif rate>=80:
##     t.write("집이 코 앞인데 !! ♬",False,"center",font = ("Arial",15,"normal"))
##elif rate >=60:
##     t.write("집에 가고 싶어 !! ♬",False,"center",font = ("Arial",15,"normal"))
##else:
##     t.color('black')
##     t.right(360)
##     t.write("거북이가 쓰러졌어요 ㅠ_ㅠ",False,"center",font = ("Arial",15,"normal"))
##     turtle.done()

from random import *
a=[1,2,3,4,5,6,7,8,9,10]
b=choices(a, [2,2,2,2,2,2,1009,2,2,2],k=3)
print(b)
if 3==b.count(7):
     print("Lucky!")
elif b.count(7)==2:
     print("Good~")
else:
     print("So so.")

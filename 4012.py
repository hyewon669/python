##t1 = (1,)
##t2 =(4,5,6)
##print(t1 + t2)
##print(t2*2)
##print(t2[0])
##print(t2[1:3])
##del t2[0]

##a = "Carpe Diem!"
##b =[1,2,3,4,5,6]
##print(len(a))
##print(len(b))


##d={'name' : 'Jane' , 'name' : 'Mason', 'age' : 12, 'number' : 123456}
##print(d)
##print(d['age'])

##d={'a' : 1, 'b' : 2}
##d['c'] = 3
##del d['a']
##print(d)

##a={'a' : 1,'b':2,'c':3,'d':4}
##print(a.keys())
##print(a.values())
##print(a.items())
##a.clear()
##print(a)

##a= set([1,2,3])
##a.add(4)
##print(a)
##a.update('abc')
##print(a)
##a.remove('c')
##print(a)

##import turtle
##t= turtle.Turtle()
##
##t.fillcolor('red')
##t.begin_fill()
##t.right(60)
##t.circle(25,180)
##t.right(120)
##t.circle(25,180)
##t.right(120)
##t.circle(25,180)
##t.right(120)
##t.circle(25,180)
##t.right(120)
##t.circle(25,180)
##t.right(120)
##t.circle(25,180)
##t.end_fill()
##
##t.fillcolor('yellow')
##t.begin_fill()
##t.right(60)
##t.circle(50)
##t.end_fill()
##turtle.done()

##import turtle
##t=turtle.Turtle()
##s=turtle.textinput('즐거운 씨큐브 코딩','이름은 알려주세요')
##t.write("%s님 반갑습니다^^"%s)
##turtle.done()

##import turtle
##t=turtle.Turtle(shape = "turtle")
##s = "즐거운 씨큐브 코딩"
##n=turtle.numinput(s,"앞으로 얼마나 이동할까요?")
##t.forward(n)
##ang = turtle.numinput(s, "오른쪽으로 얼마나 회전할까요? :", default = 0, minval=0, maxval=360)
##t.right(ang)
##turtle.done()

##t1=(1,)
##t2=(2,3,4)
##print(t1+t2)

##s1=set(['a','b','c','c','d','e','a'])
##print(s1)

##a={'a':90,'b':85,'c':95}
##a['e']=70
##a['a']=100
##print(a)
##
##d={'plus' : ['더하기','장점'] , 'minus' : ['빼기','적자'],
##   'multiply' : ['곱하다','다양하게'],'devision' : ['나누기','분열']}
##a=input('단어:')
##print(d[a])

d={'plus' : ['더하기','장점'] , 'minus' : ['빼기','적자'],
   'multiply' : ['곱하다','다양하게'],'devision' : ['나누기','분열']}
print(d.keys())

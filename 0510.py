##sum=0
##i=1
##while i <= 100:
##     sum +=i
##     i += 1
##print(sum)

##while True :
##     ans = input("Shall we close? (y/n)")
##     if ans == 'y' :
##          print("The end")
##          break

##ans=' '
##while ans != "Yes":
##     ans = input("Are you ready?")
##print("going out")

##i=1
##while i <=100:
##     print(i, end =' ' )
##     i+=1

##i=int(input("정수입력 :"))
##sum=0
##n=1
##while n<=i:
##     sum+=n
##     n+=1

##i=1
##while i<=5:
##     j=int(input("input: "))
##     i+=1
##     if j % 5 ==0:
##          continue
##     print("output: %d" %j)

##while True:
##     i=int(input())
##     if i==0:
##          break

##cnt = 0
##n = int(input("정수 입력: "))
##while True:
##     cnt +=1
##     n //=10
##     if n<=0:
##          break

##import sys
##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((400,300))
##pygame.display.set_caption("Tick Tock Timer")
##CLOCK = pygame.time.Clock()
##sysfont = pygame.font.SysFont(None,36)
##timer = 0
##while True:
##     for event in pygame.event.get():
##          if event.type == QUIT:
##               pygame.quit()
##               sys.exit()
##     timer +=1
##     screen.fill((255,255,255))
##     cnt_txt=sysfont.render("Timer : %d" %timer, True, (0,0,0))
##     screen.blit(cnt_txt, (140,140))
##     pygame.display.update()
##     CLOCK.tick(1)

##n=1
##while n <= 20 :
##     if n%10==3 or n%10==6 or n%10==9:
##          print('X',end = ' ')
##     else :
##          print(n,end = ' ')
##     n += 1

##import turtle
##import random
##
##i=1
##t=turtle.Turtle('turtle')
##while i<=30:
##     dist = random.randint(1,100)
##     ang =random.randint(-180,180)
##     t.forward(dist)
##     t.right(ang)
##     i+=1

##i=int(input())
##j=1
##while(j<=9):
##     print("%d * %d=%d"%(i,j,i*j))
##     j+=1

##from random import*
##com=randint(1,100)
##while True:
##     i=int(input())
##     if i==com:
##          print("correct!")
##          break
##     elif i<com:
##          print("up")
##     elif i>com:
##          print("down")

import sys
import pygame
from random import*
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("pygame window")
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None,36)
timer = 0
while True:
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit()
               sys.exit()
     timer +=1
     screen.fill((255,255,255))
     cnt_txt=sysfont.render("Hi!", True, (0,0,0))
     screen.blit(cnt_txt, (randint(0,400),randint(0,300)))
     pygame.display.update()
     CLOCK.tick(1)

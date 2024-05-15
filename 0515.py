##for i in range(1,11):
##    print("%d"%i)

##n=int(input())
##for i in range(1,n+1):
##    print(i)

##for i in range(1,101):
##    if i%2==0:
##        print(i)

##a=input()
##for i in range(5):
##    print(a,end="")

##n= int(input())
##for i in range(n,50):
##    print(i)

##sum = 0
##h_list = [159,163,173,158,169]
##for  h in h_list :
##    sum +=h
##print("sum : %d" % sum)
##print("avg : %.2f" %(sum/len(h_list)))

##sum=0
##for i in range(1,6):
##    n=int(input())
##    sum+=n
##print("sum:%d"%sum)
##print("avg : %.2f"%(sum/5))

import sys
import pygame
from pygame.locals import *
pygame.init()
SURFACE=pygame.display.set_mode((400,300))
CLOCK=pygame.time.Clock()
BLACK =(0,0,0)
WHITE=(255,255,255)
RED = (255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
while True :
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    SURFACE.fill(WHITE)
    rex=Rect(20,10,60,40)
    pygame.draw.rect(SUPFACE.RED.rec)
    pygame.draw.circle(SURFACE.GREEN, (120,50),10)
    pygame.draw.polygon(SUPRFACE.BULE[[50,50],[0,100,],[100,100]])
    pygame.draw.line(SURFACE.BLACK,[120,0],[120,100])
    pygame.display.update()
    CLOCK.tick(1)


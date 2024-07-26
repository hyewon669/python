from tkinter import*

##win=Tk()
##canvas = Canvas(win, bg = "yellow", width = 100, height=100)
##canvas.pack()
##win.mainloop()

##win=Tk()
##canvas=Canvas(win,bg="white",width=500,height=500)
##canvas.create_line(250,100,250,400,fill="red",width=5)
##canvas.pack(fill="both",expand=True)
##win.mainloop()

##win=Tk()
##canvas=Canvas(win,bg="white",width=495,height=100)
##canvas.pack()

##x1, y1=0,0
##x2, y2=500,0
##
##for i in range(3) :
##     y1 += 30
##     y2 = y1
##     canvas.create_line(x1,y1,x2,y2,fill="red",width = 3)
##
##win.mainloop()

##x=0
##y2=100
##y1=0
##for i in range(10):
##     x+=45
##     canvas.create_line(x,y1,x,y2,fill="red",width=3)
##
##win .mainloop()

##win=Tk()
##canvas=Canvas(win,bg="white",width=453,height=453)
##canvas.pack()
##
##bx1=3
##bx2=453
##by=3
##for i in range(10):
##     canvas.create_line(bx1,by,bx2,by,fill="blue",width=3)
##     by+=50
##
##rx=3
##ry1=3
##ry2=453
##for j in range(10):
##     canvas.create_line(rx,ry1,rx,ry2,fill="red",width=3)
##     rx+=50
##
##win.mainloop()
##pen_color="black"
##
##def paint(event):
##     global pen_color
##     x1,y1=event.x,event.y
##     x2,y2=x1+5,y1+5
##     canvas.create_line(x1,y1,x2,y2,width=3,fill=pen_color)
##
##def change_color():
##     global pen_color
##     pen_color = "red"
##
##win = Tk()
##canvas=Canvas(win,bg="white",width=500,height=200)
##btn=Button(win,text="red",command=change_color)
##canvas.pack()
##btn.pack()

win=Tk()
pen_color="black"
pen_size=5
def paint(event):
     global pen_color
     x1,y1=event.x,event.y
     x2,y2=x1+5,y1+5
     canvas.create_line(x1,y1,x2,y2,width=pen_size,fill=pen_color)


def change_color(color):
     global pen_color
     pen_color=color

def canvas_clear():
     canvas.delete("all")


def change_size(pen):
     global pen_size
     if pen == "plus":
          pen_size +=1
     elif pen == "minus":
          pen_size -=1
          if pen_size <1:
               pen_size=1

canvas=Canvas(win,bg="white",width=500,height=500)
btn_white=Button(win,text='white',bg="white",width=6,command=lambda:change_color("white"))
btn_black=Button(win,text='black',bg="black",fg="white",width=6,command=lambda:change_color("black"))
btn_blue=Button(win,text='blue',bg="blue",fg="white",width=6,command=lambda:change_color("blue"))
btn_green=Button(win,text='green',bg="green",fg="white",width=6,command=lambda:change_color("green"))
btn_yellow=Button(win,text='yellow',bg="yellow",width=6,command=lambda:change_color("yellow"))
btn_red=Button(win,text='red',bg="red",fg="white",width=6,command=lambda:change_color("red"))
btn_plus=Button(win,text="+",bg="white",width=6,command=lambda:change_size("plus"))
btn_minus=Button(win,text="-",bg="white",width=6,command=lambda:change_size("minus"))
btn_clear=Button(win,text="clear",bg="white",width=6,command=canvas_clear)



canvas.grid(row=0,column=0,columnspan=9)
btn_white.grid(row=1,column=0)
btn_black.grid(row=1,column=1)
btn_blue.grid(row=1,column=2)
btn_green.grid(row=1,column=3)
btn_yellow.grid(row=1,column=4)
btn_red.grid(row=1,column=5)
btn_plus.grid(row=1,column=6)
btn_minus.grid(row=1,column=7)
btn_clear.grid(row=1,column=8)
win.bind("<B1-Motion>",paint)
win.mainloop()

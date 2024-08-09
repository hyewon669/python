##from tkinter import*
##win=Tk()
##canvas=Canvas(win,width = 400,height=200,bg="white")
##canvas.pack()
##canvas.create_oval(10,10,60,60,fill="blue")
##canvas.create_rectangle(100,10,160,60,fill="yellow",outline="red")
##canvas.create_polygon(200,110,130,190,260,190,fill="red")
##win.mainloop()

##canvas=Canvas(win,width=200,height=200,bg="white")
##x1,y1=0,0
##x2,y2=0,200
##for i in range(9):
##     x1+=20
##     x2=x1
##     canvas.create_line(x1,y1,x2,y2)
##x1,y1=0,0
##x2,y2=200,0
##for i in range(9):
##     y1+=20
##     y2=y1
##     canvas.create_line(x1,y1,x2,y2)
##canvas.create_polygon(40,20,40,180,160,180,fill="red")
##canvas.pack()
##

##from random import*
##def draw_shape(event):
##     color=["black","white","blue","red","green","yellow"]
##     x1,y1=event.x,event.y
##     x2,y2=x1+randint(10,70),y1+randint(10,70)
##     canvas.create_oval(x1,y1,x2,y2,fill=color[randint(0,5)])
##
##win=Tk()
##canvas=Canvas(win,width=300,height=300,bg="white")
##canvas.pack()
##canvas.bind("<Double-Button-1>",draw_shape)
##win.mainloop()

##def draw_shape(event):
##     color=["black","white","blue","red","green","yellow"]
##     x1,y1=event.x,event.y
##     x2,y2=x1+25,y1+25
##     x3,y3=x1-25,y2
##     canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill="green")
##
##win=Tk()
##canvas=Canvas(win,width=300,height=300,bg="white")
##canvas.pack()
##canvas.bind("<Double-Button-1>",draw_shape)
##win.mainloop()
##


from tkinter import*
win=Tk()
pen_color="black"
pen_size=2
shape_size=10
my_tool="pen"
fill_color="white"


canvas=Canvas(win,width=350,height=350,bg="white")

def paint(event):
     global pen_size
     global pen_color
     x1,y1=event.x,event.y
     x2,y2=event.x+pen_size,event.y+pen_size
     canvas.create_line(x1,y1,x2,y2,width=pen_size,fill=pen_color)



def change_color(color):
     global pen_color
     global fill_color
     global my_tool
     if my_tool=="pen":
          pen_color=color


btn_black=Button(win,text = "black",width=8,bg="black",fg="white",command=lambda:change_color("black"))
btn_blue=Button(win,text = "blue",width=8,bg="blue",fg="white",command=lambda:change_color("blue"))
btn_green=Button(win,text = "green",width=8,bg="green",fg="white",command=lambda:change_color("green"))
btn_white=Button(win,text = "white",width=8,bg="white",command=lambda:change_color("white"))
btn_red=Button(win,text = "red",width=8,bg="red",fg="white",command=lambda:change_color("red"))
btn_yellow=Button(win,text = "yellow",width=8,bg="yellow",command=lambda:change_color("yellow"))

btn_canvas=Button(win,text="canvas\ncolor",width=8,bg="white")
btn_pen=Button(win,text="pen\ncolor",width=8,bg="black",fg="white")
btn_fill=Button(win,text="fill\ncolor",width=8,bg="white")

btn_plus=Button(win,text="+",width=8,bg="white")
btn_minus=Button(win,text="-",width=8,bg="white")
btn_clear=Button(win,text="clear",width=8,bg="white")

btn_oval=Button(win,text="○",width=8,bg="white")
btn_rect=Button(win,text="□",width=8,bg="white")
btn_poly=Button(win,text="△",width=8,bg="white")

canvas.grid(row=0,column=0,columnspan=5)
btn_canvas.grid(row=1,column=0)
btn_black.grid(row=1,column=1)
btn_blue.grid(row=1,column=2)
btn_green.grid(row=1,column=3)
btn_plus.grid(row=1,column=4)
btn_pen.grid(row=2,column=0)
btn_white.grid(row=2,column=1)
btn_red.grid(row=2,column=2)
btn_yellow.grid(row=2,column=3)
btn_minus.grid(row=2,column=4)
btn_fill.grid(row=3,column=0)
btn_oval.grid(row=3,column=1)
btn_rect.grid(row=3,column=2)
btn_poly.grid(row=3,column=3)
btn_clear.grid(row=3,column=4)

win.bind("<B1-Motion>",paint)
win.mainloop()

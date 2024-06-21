##def even(n):
##
##     if n==0:
##          return n
##     if n%2==0:
##          print(n,end=' ')
##     even(n-1)
##even(10)

##def sum(n):
##     if n==0:
##          return 0
##     else:
##          return n + sum(n-1)
##n=int(input())
##sum(n)

##from tkinter import *
##win = Tk()
##label1=Label(win,text="one")
##label2=Label(win,text="two")
##label3=Label(win,text="three")
##label1.pack()
##label2.pack()
##label3.pack()
##win.mainloop()

##from tkinter import*
##win = Tk()
##lbl1=Label(win,text = "orange",width=20,height=3,relief="solid")
##lbl2=Label(win,text= "banana",font = ("Elephant",40),bg="yellow")
##lbl3=Label(win,text="apple",fg = "red")
##lbl1.pack()
##lbl2.pack()
##lbl3.pack()
##win.mainloop()
##
##from tkinter import *
##win = Tk()
##img=PhotoImage(file='pizza.png')
##lbl=Label(win,image=img)
##lbl1=Label(win,text="pizza",bg="yellow",fg="red")
##lbl.pack()
##lbl1.pack()

##from tkinter import *
##win=Tk()
##btn=Button(win,text="Button")
##btn.pack()
##win.mainloop()
##win.mainloop()

##from tkinter import*
##win = Tk()
##def click():
##     if btn['text']=="red":
##          btn['text']="blue"
##          btn['bg']="blue"
##     else:
##          btn['text']="red"
##          btn['bg']="red"
##btn=Button(win, text = "red",fg = "white",bg="red",command=click)
##btn.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##lbl=Label(win,text="hello",bg="orange")
##lbl.pack()
##def click():
##     if lbl['text']=="hello":
##          lbl['text']="python"
##          lbl['bg']="green"
##     else:
##          lbl['text']="hello"
##          lbl['bg']="orange"
##btn=Button(win,text="Button",command=click)
##btn.pack()

##from tkinter import*
##win=Tk()
##def message(event):
##     lbl['text']=entry.get()
##entry=Entry(win)
##entry.bind("<Return>",message)
##entry.pack()
##lbl=Label(win,text=" ")
##lbl.pack()
##win.mainloop()

from tkinter import*
win=Tk()
win.title("grid")
label1=Label(win,width = 10,height = 5,bg = "red")
label2=Label(win,width = 10,height = 5,bg = "orange")
label3=Label(win,width = 10,height = 5,bg = "yellow")
label4=Label(win,width = 10,height = 5,bg = "green")
label5=Label(win,width = 10,height = 5,bg = "blue")
label6=Label(win,width = 10,height = 5,bg = "purple")

label1.grid(row=0,column =0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)
label4.grid(row=1,column=0)
label5.grid(row=1,column=1)
label6.grid(row=1,column=2)
win.mainloop()

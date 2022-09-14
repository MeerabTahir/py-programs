import math
from tkinter import*
m=Tk()
import math
def table():
    tno=int(e1.get())
    trange=int(e2.get())
    for i in range(trange+1):
        z=tno,"*",i,"=",tno*i
        Label(m,text=str(z),bg="light blue",fg="black",width=13,font=("Aerial",10)).grid(row=2+i,column=4,padx=15)

def fact():
    x=int(e1.get())
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    Label(m,bg="light blue",fg="black",width=18,text="The factorial of " +str(x)+ " is"  + str(fact),font=("Aerial",10)).grid(row=3,column=1)
def sum():
    n1=int(e1.get())
    n2=int(e2.get())
    sum=n1+n2
    Label(m,bg="light blue",fg="black",width=15,text=sum,font=("Aerial",10)).grid(row=5,column=1)

def sub():
    n1=int(e1.get())
    n2=int(e2.get())
    sub=n1-n2
    Label(m, bg="light blue",fg="black",width=15,text=sub,font=("Aerial", 10)).grid(row=6 ,column=1)

def multiply():
    n1=int(e1.get())
    n2=int(e2.get())
    multiply=n1*n2
    Label(m,bg="light blue",fg="black",width=15,text=multiply,font=("Aerial",10)).grid(row=7,column=1)

def divide():
    n1=int(e1.get())
    n2=int(e2.get())
    divide=n1/n2
    Label(m, bg="light blue", fg="black", width=15, text=divide, font=("Aerial", 10)).grid(row=8, column=1)

def sqroot():
    n1 = int(e1.get())
    sqroot=math.sqrt(n1)
    Label(m,bg="light blue",fg="black",width=15,text=sqroot,font=("Aerial",10)).grid(row=9,column=1)

def sin():
    n1 = int(e1.get())
    sin = math.sin(n1)
    Label(m, bg="light blue", fg="black", width=15, text=sin, font=("Aerial", 10)).grid(row=10, column=1)

def cos():
    n1 = int(e1.get())
    cos = math.cos(n1)
    Label(m, bg="light blue", fg="black", width=15, text=cos, font=("Aerial", 10)).grid(row=11, column=1)

def tan():
    n1 = int(e1.get())
    tan = math.tan(n1)
    Label(m, bg="Light blue", fg="black", width=15, text=tan, font=("Aerial", 10)).grid(row=12, column=1)


l1=Label(m,bg="yellow",fg="Black",text="Number1:",font=("aerial",10)).grid(row=0,column=0)
l2=Label(m,bg="yellow",fg="Black",text="Number2:",font=("aerial",10)).grid(row=1,column=0)

e1=Entry(m,bg="light green",fg="black",width=15)
e1.grid(row=0,column=1)
e2=Entry(m,bg="light green",fg="black",width=15)
e2.grid(row=1,column=1)

b1=Button(m,bg="pink",fg="black",text="factorial",command=fact,width=10,height=2)
b1.grid(row=3,column=2)
b2=Button(m,bg="pink",fg="black",text="table",command=table,width=10,height=2)
b2.grid(row=4,column=2)
b3=Button(m,bg="pink",fg="black",text="sum",command=sum,width=10,height=2)
b3.grid(row=5,column=2)
b4=Button(m,bg="pink",fg="black",text="sub",command=sub,width=10,height=2)
b4.grid(row=6,column=2)
b5=Button(m,bg="pink",fg="black",text="multiply",command=multiply,width=10,height=2)
b5.grid(row=7,column=2)
b6=Button(m,bg="pink",fg="black",text="divide",command=divide,width=10,height=2)
b6.grid(row=8,column=2)
b7=Button(m,bg="pink",fg="black",text="sqroot",command=sqroot,width=10,height=2)
b7.grid(row=9,column=2)
b8=Button(m,bg="pink",fg="black",text="sin",command=sin,width=10,height=2)
b8.grid(row=10,column=2)
b9=Button(m,bg="pink",fg="black",text="cos",command=cos,width=10,height=2)
b9.grid(row=11,column=2)
b10=Button(m,bg="pink",fg="black",text="tan",command=tan,width=10,height=2)
b10.grid(row=12,column=2)

m.mainloop()


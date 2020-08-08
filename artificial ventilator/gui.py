from tkinter import*
import tkinter.messagebox
import serial
port=serial.Serial('COM6',9600)
top = Tk()
top.title("Prototype Arificial Ventilator")
frame=Frame(top, width=1000, height=800)

logo = PhotoImage(file="bhavini.png")
w1 = Label(top, width="135", height="135", image=logo)
w1.place(x=0,y=0)

logo1 = PhotoImage(file="logo.png")
w2 = Label(top, width="135", height="135", image=logo1)
w2.place(x=1050,y=0)


w = Label(top, text="Indicative GUI for Prototype Arificial Ventilator", foreground="blue", font=("Helvetica", 34))
w.place(x=130,y=0)
w4 = Label(top, text="Designed by BHAVINI OFFICERS ASSOCIATION (BOA)", foreground="green", font=("Helvetica", 20))
w4.place(x=225,y=70)



t1=Label(top,text="Holding Time for PIP (in ms)",font=('Comic Sans MS',10))
t1.place(x=100,y=150)

e=Entry(top,font=('Helvetica',11),width="20")
e.place(x=300,y=150)

t2=Label(top,text="Holding Time for PEEP (in ms)",font=('Comic Sans MS',10))
t2.place(x=100,y=180)

e1=Entry(top,font=('Helvetica',11),width="20")
e1.place(x=300,y=180)

p1=Label(top,text="Positive Inspiratory Pressure(max) (in kPa)",font=('Comic Sans MS',10))
p1.place(x=575,y=150)

e2=Entry(top,font=('Helvetica',11),width="20")
e2.place(x=850,y=150)


p2=Label(top,text="Positive End Expiratory Pressure (in kPa)",font=('Comic Sans MS',10))
p2.place(x=575,y=180)

e3=Entry(top,font=('Helvetica',11),width="20")
e3.place(x=850,y=180)

def set1():
    if int(e.get()) not in range(0,1000):
        tkinter.messagebox.showerror("Incorrect Value","Time should lie in the range 0 to 999 ms. ")
    else:
        x1=int(e.get())+4000
        print(x1)
        data=str(x1)
        port.write(data.encode('utf-8'))

def set2():
    if int(e1.get()) not in range(0,1000):
        tkinter.messagebox.showerror("Incorrect Value","Time should lie in the range 0 to 999 ms. ")
    else:
        x2=int(e1.get())+5000
        print(x2)
        data=str(x2)
        port.write(data.encode('utf-8'))

def set3():
    if int(e2.get()) not in range(0,1000):
        tkinter.messagebox.showerror("Incorrect Value","The value of pressure should lie in the range 0 to 999 kPa. ")
    else:
        x3=int(e2.get())+3000
        print(x3)
        data=str(x3)
        port.write(data.encode('utf-8'))

def set4():
    if int(e3.get()) not in range(0,1000):
        tkinter.messagebox.showerror("Incorrect Value","The value of pressure should lie in the range 0 to 999 kPa. ")
    else:
        x4=int(e3.get())+2000
        print(x4)
        data=str(x4)
        port.write(data.encode('utf-8'))

b1=Button(top, text="Set", command=set1).place(x=500,y=145)
b2=Button(top, text="Set", command=set2).place(x=500,y=180)
b3=Button(top, text="Set", command=set3).place(x=1040,y=145)
b4=Button(top, text="Set", command=set4).place(x=1040,y=180)


w = Text(top, bg= 'blue', foreground="white", font="Helvetica", height= 10 ,width=1000 )
w.place(x=0,y=350)
w.insert('1.5',"Developed By")
w.insert(INSERT,"\n")
w.insert('2.5',"1. Chahat Jain, Birla Institute of Technology and Science Pilani, Pilani Campus")
w.insert(INSERT,"\n")
w.insert('3.5',"2. Sharan R, St.Joseph's College of Engineering Chennai")
w.insert(INSERT,"\n")
w.insert(INSERT,"\n")
w.insert('5.5',"Under the guidance of")
w.insert(INSERT,"\n")
w.insert('6.7',"Shri Sitangshu Sekhar Biswas")
w.insert(INSERT,"\n")
w.insert('7.7',"Shri Avik Kumar Saha")
w.insert(INSERT,"\n")


def start():
    s=1001
    print(s)
    port.write(b'1001')


def stop():
    s=1002
    print(s)
    port.write(b'1002')


def readyfornewrun():
    s=1003
    print(s)
    port.write(b'1003')


frame1 = Frame(top,height=500, width =1000)
frame1.place(bordermode=INSIDE,x=550,y=250)

button=Button(frame1, text="Start", command=start).grid(row=500,column=0)
button1=Button(frame1, text="Stop", command=stop).grid(row=500, column= 10)
button2=Button(frame1, text="Ready for New Run", command=readyfornewrun).grid(row=600, column= 5)

top.mainloop()

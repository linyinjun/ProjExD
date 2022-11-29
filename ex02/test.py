import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("计算器")
root.geometry("200x250+200+300")
root.resizable(False,False)

V1 = StringVar()
tk.Entry(root,textvariable=V1).place(x=16,y=15,width=168,height=30)
V1.set("0")

opt=0
ope=""
save=0
def one(event):
    global opt,ope,save
    if event.widget["text"] in ["1","2","3","4","5","6","7","8","9","0"]:
        opt=opt*10+int(event.widget["text"])
        V1.set(str(opt))
    elif event.widget["text"] in ["+","-","*","/"]:
        save=opt
        ope=event.widget["text"]
        opt=0
        V1.set("0")
    elif event.widget["text"]=="C":
        opt=0
        V1.set("0")
    elif event.widget["text"]=="=":
        if ope=="+":
            V1.set(str(opt+save))
        elif ope=="-":
            V1.set(str(save-opt))    
        elif ope=="*":
            V1.set(str(save*opt))    
        elif ope=="/":
            V1.set(str(save//opt))   

strBtns = ["1","2","3","+",
           "4","5","6","-",
           "7","8","9","*",
           "C","0","=","/"]

for i in range(16):
    V2 = StringVar()
    V2.set(strBtns[i])
    b = tk.Button(root,textvariable=V2,width=2)
    b.place(x=i%4*45+10,y=i//4*45+60,width=45,height=45)
    b.bind("<Button-1>",one)

mainloop()

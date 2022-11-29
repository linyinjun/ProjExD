import tkinter as tk 
import tkinter.messagebox as tkm

#練習3  
def button_click(event):
    btn = event.widget
    i = btn["text"]
    if i == "=":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    else:
    #tkm.showinfo(txt,f"[{txt}]ボタンがクリックされました")
        #6
        entry.insert(tk.END, i)
    if i =="AC":
         entry.delete(0,tk.END)
         entry.insert(tk.END)
    
#練習1
root = tk.Tk()
root.title("calc")
root.geometry("450x500")

#練習4
entry = tk.Entry(root, justify="right",width=10,font=("",40))
entry.grid(row=0, column=0, columnspan=3)

#練習2
r, c = 2, 2 
for i in range(9,-1,-1):
    if i == 0:
        button = tk.Button(root, text=f"{i}", width=4, height=2, font=("",30))
        button.grid(row=5,column=0)
    else:
        button = tk.Button(root, text=f"{i}", width=4, height=2, font=("",30))
        button.grid(row=r,column=c)
    
    button.bind("<1>",button_click)
    c -= 1
    if c == -1:
        r += 1
        c = 2
button = tk.Button(root, text=f"00", width=4, height=2, font=("",30))
button.grid(row=5,column=1)
button.bind("<1>",button_click)

#5
operatos=["/", "*", "-", "+", "=","."]
r, c=1, 3
for ope in operatos:
    if ope == ".":
        button = tk.Button(root, text=f".", width=4, height=2, font=("",30))
        button.grid(row=5,column=2)     
    else:
         button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("",30))
         button.grid(row=r,column=c)

    
    button.bind("<1>",button_click)
    if c%3== 0:
        r += 1

    
symbols=["AC"]
r, c=1, 2
for sym in symbols:
    button = tk.Button(root, text=f"{sym}", width=4, height=2, font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c += 1

root.mainloop()
import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import sample as sp

global ct
ct = True
    
def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key,ct
    key = ""
    if cx == 1350 and cy == 750 and ct == True:#ゴールの設置
        tkm.showwarning(root," ゴール")
        cl = None
                



def main_proc():
    global cx, cy, mx, my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 1: # 移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1        
    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    label = tk.Label(root, font=("",80))
    label.pack()

    tmr = 0
    jid = None

    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)

    sx, sy =1*100+50,1*100+50#スタートのイラスト
    z = tk.PhotoImage(file="fig/0.png")
    canvas.create_image(sx, sy, image=z)

    gx, gy = 1350 ,750#ゴールのイラスト
    zu = tk.PhotoImage(file="fig/6.png")
    canvas.create_image(gx, gy, image=zu)

    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    tori = tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    
    key = ""
    tmr = 0
    jid = None
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()
    

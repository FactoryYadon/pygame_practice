from tkinter import *
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(folder_path,"images")



root = Tk()
root.title("kkh GUI")                                                                   # 타이틀 입력
root.geometry("640x480+300+100")                                                        # 가로*세로 + X좌표 + y좌표

listbox = Listbox(root , selectmode = "extended", height = 3)                           # extended 여러개 선택 가능 , single 한개만 선택 가능
listbox.insert(0, "사과")
listbox.insert(1 ,"딸기")
listbox.insert(2 ,"바나나")
listbox.insert(END ,"수박")
listbox.insert(END ,"포도")
listbox.pack()

def btncmd():
    pass

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()

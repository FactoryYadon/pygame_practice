from tkinter import *
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(folder_path,"images")



root = Tk()
root.title("kkh GUI")                                                                   # 타이틀 입력
root.geometry("640x480+300+100")                                                        # 가로*세로 + X좌표 + y좌표

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width = 30)                                                             # 줄 변환 불가 text
e.pack()
e.insert(END,"한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0",END))                                                           # 처음부터 끝까지 1: 첫번째 라인 0: 첫번째 열
    print(e.get())
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()

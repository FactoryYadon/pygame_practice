from tkinter import *
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(folder_path,"images")



root = Tk()
root.title("kkh GUI")                                                                   # 타이틀 입력
root.geometry("640x480+300+100")                                                        # 가로*세로 + X좌표 + y좌표

label1 = Label(root, text="안녕하세요")
label1.pack()

label2_photo = PhotoImage(file=os.path.join(image_folder_path,"checkbox.png"))
label2 = Label(root, image = label2_photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global label2_photo
    label2_photo = PhotoImage(file=os.path.join(image_folder_path,"checkbox2.png"))

btn = Button(root , text="클릭" , command = change)
btn.pack()

def change2():
    label2.config(image = label2_photo)
    

btn2 = Button(root , text="클릭" , command = change2)
btn2.pack()


root.mainloop()

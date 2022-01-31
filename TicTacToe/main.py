from tkinter import *
import gameplay
root = Tk()

root.title('tictactoe')
root.geometry("400x400")
root.configure(bg="red")
 

frame = LabelFrame(root,borderwidth = 1, bg="orange", padx=5, pady=5)
frame.grid(row=1, column=0,columnspan=6, padx=5, pady=5)


def mode():
    
    for widgets in frame.winfo_children():
        widgets.destroy()
            
    easy_button = Button(frame, text="EASY",bg="red",width=50 , command=gameplay.easy).grid(row =0 , column=0, pady =10)
    normal_button = Button(frame, text="NORMAL",bg="red",width=50, command=gameplay.normal).grid(row =1 , column=0, pady=10)
    easy_button = Button(frame, text="HARD",bg="red",width=50, command=gameplay.hard).grid(row =2 , column=0 ,pady= 10)

welcome_label =Label(frame, text="welcome to Tic Tac Toe",font=("Times New Roman", 29),bg="red") 
welcome_label.grid(row=0,column=0,columnspan= 3,pady=(0,20))

play_as_label = Label(frame , text="play VS :",bg="orange",padx=1).grid(row =1 , column=0)

def clear_frame():
       for widgets in frame.winfo_children():
            widgets.destroy()

Human_button = Button(frame, text="Human",bg="orange",width=20 , command= gameplay.human).grid(row =1 , column=1)
Computer_button = Button(frame, text="Computer",bg="orange",width=20, command= mode).grid(row =1 , column=2)


root.mainloop()
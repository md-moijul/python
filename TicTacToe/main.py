from cProfile import label
from tkinter import *
import copy

root = Tk()

root.title('tictactoe')
root.geometry("500x500")
root.configure(bg="red")

symble ="X"
turn=1
numbers = ["1","2","3","4","5","6","7","8","9"]

frame = LabelFrame(root,borderwidth = 1, bg="orange", padx=5, pady=5)
frame.grid(row=2, column=0,columnspan=6, padx=5, pady=5)

frame1 = LabelFrame(root,borderwidth = 1, bg="orange", padx=5, pady=5)
frame1.grid(row=1, column=0,columnspan=6, padx=5, pady=5)
        
def pressed(value):
    
    global symble
    if value.isdigit() is True:
        numbers[numbers.index(value)] = symble
        
        if symble == "X" :
            symble = "O"
        else :
            symble = "X"
        board()
        
    else :
        print(value)
        
    
def win_check():
    if numbers[0]==numbers[1] and numbers[1]==numbers[2]:
        return True
    elif numbers[3]==numbers[4] and numbers[4]==numbers[5]:
        return True
    elif numbers[6]==numbers[7] and numbers[7]==numbers[9]:
        return True
    elif numbers[0]==numbers[3] and numbers[3]==numbers[6]:
        return True
    elif numbers[1]==numbers[4] and numbers[4]==numbers[7]:
        return True
    elif numbers[2]==numbers[5] and numbers[5]==numbers[8]:
        return True
    elif numbers[0]==numbers[4] and numbers[4]==numbers[8]:
        return True
    elif numbers[2]==numbers[4] and numbers[4]==numbers[6]:
        return True
    else:
        return False
    
def status():

    for widgets in frame1.winfo_children():
            widgets.destroy()
    
    if symble == "X":
        player_no= "1"
    else:
        player_no= "2" 
        
    if symble == "X":
        winner_no= "2"
    else:
        winner_no= "1" 
       
    textstatus =("Player no "+ player_no +" make your move :")
    winstatus=("Player no "+ winner_no +"\nwon the match")
    
    if win_check() == False:
        status_label =Label(frame1, text=textstatus,font=("Times New Roman", 15), bg="orange") 
        status_label.grid(row=9,column=0,columnspan= 5)
    else :
        for widgets in frame.winfo_children():
            widgets.destroy()
            
        status_label =Label(frame1, text=winstatus,font=("Times New Roman", 50), bg="orange") 
        status_label.grid(row=9,column=0,columnspan= 5)
    
    

def board():
    for widgets in frame.winfo_children():
        widgets.destroy()
    for widgets in frame1.winfo_children():
        widgets.destroy()
        
        
    if numbers[0]== "X" :
        button1 = Button(frame, text=numbers[0],font=("Times New Roman", 10),bg="orange",fg ="blue",pady= 50,padx=50 ).grid(row =0 , column=0,pady= 2,padx=2)
    elif numbers[0]== "O" :
        button1 = Button(frame, text=numbers[0],font=("Times New Roman", 10),bg="orange",fg ="green",pady= 50,padx=50 ).grid(row =0 , column=0,pady= 2,padx=2)
    else :
        button1 = Button(frame, text=numbers[0],font=("Times New Roman", 10),bg="red",pady= 50,padx=50 ,command= lambda: pressed(numbers[0])).grid(row =0 , column=0,pady= 2,padx=2)

    
    if numbers[1]== "X" :
        button2 = Button(frame, text=numbers[1],font=("Times New Roman", 10),bg="orange",fg ="blue",pady= 50,padx=50).grid(row =0 , column=2,pady= 2,padx=2)
    elif numbers[1]== "O" :
        button2 = Button(frame, text=numbers[1],font=("Times New Roman", 10),bg="orange",fg ="green",pady= 50,padx=50).grid(row =0 , column=2,pady= 2,padx=2)
    else:
        button2 = Button(frame, text=numbers[1],font=("Times New Roman", 10),bg="red",pady= 50,padx=50,command= lambda: pressed(numbers[1])).grid(row =0 , column=2,pady= 2,padx=2)
        
    if numbers[2]== "X" :
        button3 = Button(frame, text=numbers[2],font=("Times New Roman", 10),bg="orange",fg ="blue",pady= 50,padx=50).grid(row =0 , column=4,pady= 2,padx=2)
    elif numbers[2]== "O" :
        button3 = Button(frame, text=numbers[2],font=("Times New Roman", 10),bg="orange",fg ="green",pady= 50,padx=50).grid(row =0 , column=4,pady= 2,padx=2)
    else:
        button3 = Button(frame, text=numbers[2],font=("Times New Roman", 10),bg="red",pady=50,padx=50,command= lambda: pressed(numbers[2])).grid(row =0 , column=4,pady= 2,padx=2)
    
    if numbers[3]== "X" :
        button4 = Button(frame, text=numbers[3],font=("Times New Roman", 10),bg="orange",fg ="blue",pady= 50,padx=50).grid(row =2 , column=0,pady= 2,padx=2)
    elif numbers[3]== "O" :
        button4 = Button(frame, text=numbers[3],font=("Times New Roman", 10),bg="orange",fg ="green",pady= 50,padx=50).grid(row =2 , column=0,pady= 2,padx=2)
    else:
        button4 = Button(frame, text=numbers[3],font=("Times New Roman", 10),bg="red",pady= 50,padx=50,command= lambda: pressed(numbers[3])).grid(row =2 , column=0,pady= 2,padx=2)
    
    if numbers[4]== "X" :
        button5 = Button(frame, text=numbers[4],font=("Times New Roman", 10),bg="orange",fg ="blue",pady= 50,padx=50).grid(row =2 , column=2,pady= 2,padx=2)
    elif numbers[4]== "O" :
        button5 = Button(frame, text=numbers[4],font=("Times New Roman", 10),bg="orange",fg ="green",pady= 50,padx=50).grid(row =2 , column=2,pady= 2,padx=2)
    else:
        button5 = Button(frame, text=numbers[4],font=("Times New Roman", 10),bg="red",pady= 50,padx=50,command= lambda: pressed(numbers[4])).grid(row =2 , column=2,pady= 2,padx=2)
    
    if numbers[5]== "X" :
        button6 = Button(frame, text=numbers[5],font=("Times New Roman", 10),bg="orange",fg ="blue",pady= 50,padx=50).grid(row =2 , column=4,pady= 2,padx=2)
    elif numbers[5]== "O" :
        button6 = Button(frame, text=numbers[5],font=("Times New Roman", 10),bg="orange",fg ="green",pady= 50,padx=50).grid(row =2 , column=4,pady= 2,padx=2)
    else:
        button6 = Button(frame, text=numbers[5],font=("Times New Roman", 10),bg="red",pady= 50,padx=50,command= lambda: pressed(numbers[5])).grid(row =2 , column=4,pady= 2,padx=2)
    
    if numbers[6]== "X" :
        button7 = Button(frame, text=numbers[6],font=("Times New Roman", 10),bg="orange",fg ="blue",pady= 50,padx=50).grid(row =4 , column=0,pady= 2,padx=2)
    elif numbers[6]== "O" :
        button7 = Button(frame, text=numbers[6],font=("Times New Roman", 10),bg="orange",fg ="green",pady= 50,padx=50).grid(row =4 , column=0,pady= 2,padx=2)
    else:    
        button7 = Button(frame, text=numbers[6],font=("Times New Roman", 10),bg="red",pady= 50,padx=50,command= lambda: pressed(numbers[6])).grid(row =4 , column=0,pady= 2,padx=2)
    
    if numbers[7]== "X" :
        button8 = Button(frame, text=numbers[7],font=("Times New Roman", 10),bg="orange",fg ="blue",pady= 50,padx=50).grid(row =4 , column=2,pady= 2,padx=2)
    elif numbers[7]== "O" :
        button8 = Button(frame, text=numbers[7],font=("Times New Roman", 10),bg="orange",fg ="green",pady= 50,padx=50).grid(row =4 , column=2,pady= 2,padx=2)
    else:
        button8 = Button(frame, text=numbers[7],font=("Times New Roman", 10),bg="red",pady= 50,padx=50,command= lambda: pressed(numbers[7])).grid(row =4 , column=2,pady= 2,padx=2)
    
    if numbers[8]== "X" :
        button9 = Button(frame, text=numbers[8],font=("Times New Roman", 10),bg="orange",fg ="blue",pady= 50,padx=50).grid(row =4 , column=4,pady= 2,padx=2)
    elif numbers[8]== "O" :
        button9 = Button(frame, text=numbers[8],font=("Times New Roman", 10),bg="orange",fg ="green",pady= 50,padx=50).grid(row =4 , column=4,pady= 2,padx=2)
    else:
        button9 = Button(frame, text=numbers[8],font=("Times New Roman", 10),bg="red",pady= 50,padx=50,command= lambda: pressed(numbers[8])).grid(row =4 , column=4,pady= 2,padx=2)
    
    
    
    status()
    reset_button = Button(frame, text="reset",bg="orange",width=20 , command= welcome).grid(row =10 , column=0, columnspan=6) 
  

def human():
    for widgets in frame.winfo_children():
        widgets.destroy()

    board()
    

def easy():
    for widgets in frame.winfo_children():
        widgets.destroy()
        
    board()
  
    
def normal():
    for widgets in frame.winfo_children():
        widgets.destroy()
    
    board()   
    

def hard():
    for widgets in frame.winfo_children():
        widgets.destroy()
    
    board()    
    

def welcome():
    global numbers
    numbers = ["1","2","3","4","5","6","7","8","9"]
    for widgets in frame.winfo_children():
        widgets.destroy()
    def mode():
        for widgets in frame.winfo_children():
            widgets.destroy()
        for widgets in frame1.winfo_children():
            widgets.destroy()
            
        easy_button = Button(frame, text="EASY",bg="red",width=50 , command=easy).grid(row =0 , column=0, pady =10)
        normal_button = Button(frame, text="NORMAL",bg="red",width=50, command=normal).grid(row =1 , column=0, pady=10)
        easy_button = Button(frame, text="HARD",bg="red",width=50, command=hard).grid(row =2 , column=0 ,pady= 10)

    welcome_label =Label(frame1, text="welcome to Tic Tac Toe",font=("Times New Roman", 29),bg="red") 
    welcome_label.grid(row=0,column=0,columnspan= 3,pady=(0,20))

    play_as_label = Label(frame , text="play VS :",bg="orange",padx=1).grid(row =1 , column=0)

    def clear_frame():
           for widgets in frame.winfo_children():
                widgets.destroy()

    Human_button = Button(frame, text="Human",bg="orange",width=20 , command= human).grid(row =1 , column=1)
    Computer_button = Button(frame, text="Computer",bg="orange",width=20, command= mode).grid(row =1 , column=2)

welcome()


root.mainloop()
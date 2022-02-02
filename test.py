from tkinter import *
import random
import time

root = Tk()

root.title('Jk tech')
root.geometry("410x500")
root.configure(bg='#967852')



numbers = ["1","2","3","4","5","6","7","8","9"]
symble ="X"
type = 0
move_no= 0


frame = LabelFrame(root,borderwidth = 1, bg='#E1CA97', padx=5, pady=5)
frame.grid(row=2, column=0,columnspan=6, padx=5, pady=5)

frame1 = LabelFrame(root,borderwidth = 1, bg='#E1CA97', padx=5, pady=5)
frame1.grid(row=1, column=0,columnspan=6, padx=5, pady=5)

def demoboard():
    board_demo = (numbers[0]+"    |    " + numbers[1]+"    |    " + numbers[2]+ "\n--------------------\n" + numbers[3]+"    |    " + numbers[4]+"    |    "+ numbers[5]+ "\n--------------------\n" +numbers[6]+"    |    "+ numbers[7]+"    |    " + numbers[8] )
    
    board_label =Label(frame1, text=board_demo,font=("Times New Roman", 25),bg='#E1CA97',padx=30, pady=30) 
    board_label.grid(row=1,column=0,columnspan= 5)
        
def pressed(value):
    global symble , move_no
    if value.isdigit() is True:
        numbers[numbers.index(value)] = symble
        move_no += 1
        if symble == "X" :
            symble = "O"
        else :
            symble = "X"
         
    if type != 0  and move_no < 9:
        if win_check() == False:
            compmove()
            move_no += 1
            
    
    board()
    
def compmove():
    global symble, move_no
    choice = 0
    
    if type == 1:
        choice = 0
        while numbers[choice].isdigit() is False:
            choice = (random.randint(0, 8))
           
        numbers[choice] = symble
        
        symble = "X"
        
    else :
        
        choice = 4

        if numbers[4].isdigit() is True : 
            choice == 4
        elif  numbers[0].isdigit() is True or numbers[2].isdigit() is True or numbers[6].isdigit() is True or numbers[8].isdigit() is True:
            while numbers[choice].isdigit() is False:
                choice = random.choice([0,2,6,8])
        elif numbers[1].isdigit() is True or numbers[3].isdigit() is True or numbers[5].isdigit() is True or numbers[7].isdigit() is True:
            while numbers[choice].isdigit() is False:
                choice = random.choice([1,3,5,7])
        
        if type == 3:
            

                if numbers[0]==numbers[1] and numbers[2].isdigit() is True:
                    choice = 2
                elif numbers[2]==numbers[1] and numbers[0].isdigit() is True:
                    choice = 0
                elif numbers[0]==numbers[2] and numbers[1].isdigit() is True:
                    choice = 1
                elif numbers[3]==numbers[4] and numbers[5].isdigit() is True:
                    choice = 5
                elif numbers[4]==numbers[5] and numbers[3].isdigit() is True:
                    choice = 3
                elif numbers[3]==numbers[5] and numbers[4].isdigit() is True:
                    choice = 4
                elif numbers[6]==numbers[7] and numbers[8].isdigit() is True:
                    choice = 8 
                elif numbers[7]==numbers[8] and numbers[6].isdigit() is True:
                    choice = 6
                elif numbers[6]==numbers[8] and numbers[7].isdigit() is True:
                    choice = 7
                elif numbers[0]==numbers[4] and numbers[8].isdigit() is True:
                    choice = 8
                elif numbers[4]==numbers[8] and numbers[0].isdigit() is True:
                    choice = 0
                elif numbers[2]==numbers[4] and numbers[6].isdigit() is True:
                    choice = 6
                elif numbers[4]==numbers[6] and numbers[2].isdigit() is True:
                    choice = 2
                elif numbers[6]==numbers[2] and numbers[4].isdigit() is True:
                    choice = 4    
                elif numbers[0]==numbers[1] and numbers[6].isdigit() is True:
                    choice = 6
                elif numbers[3]==numbers[6] and numbers[0].isdigit() is True:
                    choice = 0
                elif numbers[0]==numbers[6] and numbers[3].isdigit() is True:
                    choice = 3
                elif numbers[1]==numbers[4] and numbers[7].isdigit() is True:
                    choice = 7
                elif numbers[4]==numbers[7] and numbers[1].isdigit() is True:
                    choice = 1
                elif numbers[1]==numbers[7] and numbers[4].isdigit() is True:
                    choice = 4
                elif numbers[2]==numbers[5] and numbers[8].isdigit() is True:
                    choice = 8 
                elif numbers[5]==numbers[8] and numbers[2].isdigit() is True:
                    choice = 2
                elif numbers[2]==numbers[8] and numbers[5].isdigit() is True:
                    choice = 5

    
        numbers[choice] = symble
        symble = "X"  
    
    print("computer chosed"+str(choice+1))
    
    for widgets in frame1.winfo_children():
            widgets.destroy()
            print("computer chosed"+str(choice+1))
    status2_label =Label(frame1, text=("computer chosed"+str(choice+1)),font=("Times New Roman", 22), bg='#E1CA97') 
    status2_label.grid(row=1,column=0,columnspan= 5)
    print("computer chosed"+str(choice+1))
    
    time.sleep(1)

        

            
def reset():
    
        for widgets in frame.winfo_children():
            widgets.destroy()
        for widgets in frame1.winfo_children():
            widgets.destroy()
            
        global numbers, symble, move_no, type
        numbers = ["1","2","3","4","5","6","7","8","9"]
        symble ="X"
        type = 0
        move_no= 0
        welcome()
        

def win_check():
    if numbers[0]==numbers[1] and numbers[1]==numbers[2]:
        return True
    elif numbers[3]==numbers[4] and numbers[4]==numbers[5]:
        return True
    elif numbers[6]==numbers[7] and numbers[7]==numbers[8]:
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
    status_list= ["Player no "," make your move :","\nwon the match","the match has been drawn","it's your move :"," won the match!"]
    for widgets in frame1.winfo_children():
            widgets.destroy()
    
    if type == 0:
        if symble == "X":
            player_no= "1"
        else:
            player_no= "2" 
            
        if symble == "X":
            winner_no= "2"
        else:
            winner_no= "1" 
        
        
        if win_check() == False:
            if move_no < 9 :
                status_label =Label(frame1, text=(status_list[0]+ player_no +status_list[1]),font=("Times New Roman", 22), bg='#E1CA97') 
                status_label.grid(row=0,column=0,columnspan= 5)
            else:
                for widgets in frame.winfo_children():
                    widgets.destroy()
                
                status_label =Label(frame1, text=status_list[3],font=("Times New Roman", 27), bg='#E1CA97') 
                status_label.grid(row=0,column=0,columnspan= 5)
                demoboard()
            
 
        else :
            for widgets in frame.winfo_children():
                widgets.destroy()

            status_label =Label(frame1, text=(status_list[0]+ winner_no + status_list[2]),font=("Times New Roman", 48), bg='#E1CA97') 
            status_label.grid(row=0,column=0,columnspan= 5)
            demoboard()
    else:
        if symble == "X":
            winner_no= "computer"
        else:
            winner_no= "You have"
        
        if win_check() == False:
            if move_no < 9:
                status_label =Label(frame1, text=status_list[4],font=("Times New Roman", 22), bg='#E1CA97') 
                status_label.grid(row=1,column=0,columnspan= 5)
                
            else:
                for widgets in frame.winfo_children():
                    widgets.destroy()
                
                status_label =Label(frame1, text=status_list[3],font=("Times New Roman", 27), bg='#E1CA97') 
                status_label.grid(row=0,column=0,columnspan= 5)
                demoboard()
        else:
            for widgets in frame.winfo_children():
                widgets.destroy()
             
            status_label =Label(frame1, text=winner_no+status_list[5],font=("Times New Roman", 28), bg='#E1CA97') 
            status_label.grid(row=0,column=0,columnspan= 5)
            demoboard()  
def board():
    for widgets in frame.winfo_children():
        widgets.destroy()
    for widgets in frame1.winfo_children():
        widgets.destroy()
        
        
    if numbers[0]== "X" :
        button1 = Button(frame, text=numbers[0],font=("Times New Roman", 25),bg='#E1CA97',fg ='#b30000',pady= 30,padx=38 ).grid(row =0 , column=0,pady= 2,padx=2)
    elif numbers[0]== "O" :
        button1 = Button(frame, text=numbers[0],font=("Times New Roman", 25),bg='#E1CA97',fg ='#1b1039',pady= 30,padx=38 ).grid(row =0 , column=0,pady= 2,padx=2)
    else :
        button1 = Button(frame, text=numbers[0],font=("Times New Roman", 25),bg='#967852',pady= 30,padx=38 ,command= lambda: pressed(numbers[0])).grid(row =0 , column=0,pady= 2,padx=2)

    
    if numbers[1]== "X" :
        button2 = Button(frame, text=numbers[1],font=("Times New Roman", 25),bg='#E1CA97',fg ='#b30000',pady= 30,padx=38).grid(row =0 , column=2,pady= 2,padx=2)
    elif numbers[1]== "O" :
        button2 = Button(frame, text=numbers[1],font=("Times New Roman", 25),bg='#E1CA97',fg ='#1b1039',pady= 30,padx=38).grid(row =0 , column=2,pady= 2,padx=2)
    else:
        button2 = Button(frame, text=numbers[1],font=("Times New Roman", 25),bg='#967852',pady= 30,padx=38,command= lambda: pressed(numbers[1])).grid(row =0 , column=2,pady= 2,padx=2)
        
    if numbers[2]== "X" :
        button3 = Button(frame, text=numbers[2],font=("Times New Roman", 25),bg='#E1CA97',fg ='#b30000',pady= 30,padx=38).grid(row =0 , column=4,pady= 2,padx=2)
    elif numbers[2]== "O" :
        button3 = Button(frame, text=numbers[2],font=("Times New Roman", 25),bg='#E1CA97',fg ='#1b1039',pady= 30,padx=38).grid(row =0 , column=4,pady= 2,padx=2)
    else:
        button3 = Button(frame, text=numbers[2],font=("Times New Roman", 25),bg='#967852', pady= 30,padx=38,command= lambda: pressed(numbers[2])).grid(row =0 , column=4,pady= 2,padx=2)
    
    if numbers[3]== "X" :
        button4 = Button(frame, text=numbers[3],font=("Times New Roman", 25),bg='#E1CA97',fg ='#b30000',pady= 30,padx=38).grid(row =2 , column=0,pady= 2,padx=2)
    elif numbers[3]== "O" :
        button4 = Button(frame, text=numbers[3],font=("Times New Roman", 25),bg='#E1CA97',fg ='#1b1039',pady= 30,padx=38).grid(row =2 , column=0,pady= 2,padx=2)
    else:
        button4 = Button(frame, text=numbers[3],font=("Times New Roman", 25),bg='#967852',pady= 30,padx=38,command= lambda: pressed(numbers[3])).grid(row =2 , column=0,pady= 2,padx=2)
    
    if numbers[4]== "X" :
        button5 = Button(frame, text=numbers[4],font=("Times New Roman", 25),bg='#E1CA97',fg ='#b30000',pady= 30,padx=38).grid(row =2 , column=2,pady= 2,padx=2)
    elif numbers[4]== "O" :
        button5 = Button(frame, text=numbers[4],font=("Times New Roman", 25),bg='#E1CA97',fg ='#1b1039',pady= 30,padx=38).grid(row =2 , column=2,pady= 2,padx=2)
    else:
        button5 = Button(frame, text=numbers[4],font=("Times New Roman", 25),bg='#967852',pady= 30,padx=38,command= lambda: pressed(numbers[4])).grid(row =2 , column=2,pady= 2,padx=2)
    
    if numbers[5]== "X" :
        button6 = Button(frame, text=numbers[5],font=("Times New Roman", 25),bg='#E1CA97',fg ='#b30000',pady= 30,padx=38).grid(row =2 , column=4,pady= 2,padx=2)
    elif numbers[5]== "O" :
        button6 = Button(frame, text=numbers[5],font=("Times New Roman", 25),bg='#E1CA97',fg ='#1b1039',pady= 30,padx=38).grid(row =2 , column=4,pady= 2,padx=2)
    else:
        button6 = Button(frame, text=numbers[5],font=("Times New Roman", 25),bg='#967852',pady= 30,padx=38,command= lambda: pressed(numbers[5])).grid(row =2 , column=4,pady= 2,padx=2)
    
    if numbers[6]== "X" :
        button7 = Button(frame, text=numbers[6],font=("Times New Roman", 25),bg='#E1CA97',fg ='#b30000',pady= 30,padx=38).grid(row =4 , column=0,pady= 2,padx=2)
    elif numbers[6]== "O" :
        button7 = Button(frame, text=numbers[6],font=("Times New Roman", 25),bg='#E1CA97',fg ='#1b1039',pady= 30,padx=38).grid(row =4 , column=0,pady= 2,padx=2)
    else:    
        button7 = Button(frame, text=numbers[6],font=("Times New Roman", 25),bg='#967852',pady= 30,padx=38,command= lambda: pressed(numbers[6])).grid(row =4 , column=0,pady= 2,padx=2)
    
    if numbers[7]== "X" :
        button8 = Button(frame, text=numbers[7],font=("Times New Roman", 25),bg='#E1CA97',fg ='#b30000',pady= 30,padx=38).grid(row =4 , column=2,pady= 2,padx=2)
    elif numbers[7]== "O" :
        button8 = Button(frame, text=numbers[7],font=("Times New Roman", 25),bg='#E1CA97',fg ='#1b1039',pady= 30,padx=38).grid(row =4 , column=2,pady= 2,padx=2)
    else:
        button8 = Button(frame, text=numbers[7],font=("Times New Roman", 25),bg='#967852',pady= 30,padx=38,command= lambda: pressed(numbers[7])).grid(row =4 , column=2,pady= 2,padx=2)
    
    if numbers[8]== "X" :
        button9 = Button(frame, text=numbers[8],font=("Times New Roman", 25),bg='#E1CA97',fg ='#b30000',pady= 30,padx=38).grid(row =4 , column=4,pady= 2,padx=2)
    elif numbers[8]== "O" :
        button9 = Button(frame, text=numbers[8],font=("Times New Roman", 25),bg='#E1CA97',fg ='#1b1039',pady= 30,padx=38).grid(row =4 , column=4,pady= 2,padx=2)
    else:
        button9 = Button(frame, text=numbers[8],font=("Times New Roman", 25),bg='#967852',pady= 30,padx=38,command= lambda: pressed(numbers[8])).grid(row =4 , column=4,pady= 2,padx=2)
    
    
    
    status()
    reset_button = Button(frame, text="reset",bg='#E1CA97',width=20 , command= reset).grid(row =10 , column=0, columnspan=6) 
  

def human():
    for widgets in frame.winfo_children():
        widgets.destroy()

    board()
    

def computer(lavel):
    global type
    
    
    if lavel == 1:
        type = 1
    elif lavel == 2:
        type = 2
    elif lavel == 3:
        type = 3
    else:
        type = 0

    
    for widgets in frame.winfo_children():
        widgets.destroy()
        
    board()
  
       
    

def welcome():
    global numbers
    for widgets in frame.winfo_children():
        widgets.destroy()
    for widgets in frame1.winfo_children():
        widgets.destroy()
    def mode():
        for widgets in frame.winfo_children():
            widgets.destroy()
        for widgets in frame1.winfo_children():
            widgets.destroy()
        
        info_label =Label(frame1, text="choose the difficulty level :",font=("Times New Roman", 25),bg='#E1CA97') 
        info_label.grid(row=0,column=0,columnspan= 3,padx=5,pady=(0,20))
        easy_button = Button(frame, text="EASY",font=("Times New Roman", 15),bg='#967852',width=32, command=lambda: computer(1),pady=30).grid(row =0 , column=0,padx=7, pady =10)
        normal_button = Button(frame, text="NORMAL",font=("Times New Roman", 15),bg='#967852',width=32, command=lambda: computer(2),pady=30).grid(row =1 , column=0,padx=7, pady=10)
        easy_button = Button(frame, text="HARD",font=("Times New Roman", 15),bg='#967852',width=32, command=lambda: computer(3),pady=30).grid(row =2 , column=0,padx=7,pady= 10)

    welcome_label =Label(frame1, text="welcome to Tic Tac Toe",font=("Times New Roman", 29),bg='#967852') 
    welcome_label.grid(row=0,column=0,columnspan= 3,pady=(0,20))
    
    demoboard()

    play_as_label = Label(frame , text="play VS :",font=("Times New Roman", 15),bg='#E1CA97',padx=1).grid(row =1 , column=0)

    def clear_frame():
           for widgets in frame.winfo_children():
                widgets.destroy()

    Human_button = Button(frame, text="Human",font=("Times New Roman", 15),bg='#967852',width=12 ,pady=9, command= human).grid(row =1 , column=1,padx=5,pady=10)
    Computer_button = Button(frame, text="Computer",font=("Times New Roman", 15),bg='#967852',width=12,pady=9, command= mode).grid(row =1 , column=2,padx=5,pady=10)

welcome()


root.mainloop()
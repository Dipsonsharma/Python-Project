from tkinter import Tk, Entry,Button,StringVar
import random
class game:
    def __init__(self,master):
        master.title("Game")
        master.geometry('370x420+0+0')
        master.config(bg='#d6baa3')
        # master.resizable(False,False)

        self.equation=StringVar()
        self.myval=StringVar()
        self.cc=StringVar()


        Entry(width=22,bg='#f6efeb',fg='#4d4949',font=('Helvetica',28), textvariable=self.myval).place(x=10,y=30,width=110,height=80)

        Entry(width=22,bg='#f6efeb',fg='#4d4949',font=('Helvetica',28), textvariable=self.cc).place(x=130,y=30,width=110,height=80)

        Entry(width=22,bg='#f6efeb',fg='#4d4949',font=('Helvetica',24), textvariable=self.equation).place(x=250,y=30,width=110,height=40)
        

        Button(width=11,height=4,text='START',relief='flat',bg='#117800',font=('Helvetica',9),command=self.solve).place(x=255 ,y=75 , width=50, height=35)
        Button(width=11,height=4,text='RESET',relief='flat',bg='#be1010',font=('Helvetica',9),command=self.clear).place(x=315 ,y=75 , width=50, height=35)
        
        Button(width=11,height=4,text='✂️\nScissor',relief='flat',bg='white',font=('Helvetica',24),command=lambda:self.show('scissor')).place(x=10 ,y=160 , width=110, height=250)
        Button(width=11,height=4,text='📄\nPaper',relief='flat',bg='white',font=('Helvetica',24),command=lambda:self.show('paper')).place(x=130,y=160, width=110, height=250 )
        Button(width=11,height=4,text='🪨\nRock',relief='flat',bg='white',font=('Helvetica',24),command=lambda:self.show('rock')).place(x=250,y=160, width=110, height=250)

    def show(self,value):
        a=str(value)
        a=a.title()
        self.myval.set(a)
        self.v=value

    def clear(self):
        self.equation.set('')
        self.myval.set('')
        self.cc.set('')

    def solve(self):
            self.computer = random.choice([1,-1,0])
            con={"scissor":1, "paper":0, "rock":-1}
            revcon={ 1:"Scissor" , 0:"Paper" , -1:"Rock" }

            #computer choice
            self.cc .set(str(revcon.get(self.computer)))

            #human choice
            self.unum =con.get(self.v)

            if(self.unum == self.computer):
                self.equation.set("Draw")
            else:
                if(self.unum==1 and self.computer==0):
                        self.equation.set("You win!")
                elif(self.unum==1 and self.computer==-1):
                        self.equation.set("You lose!")
                elif(self.unum==-1 and self.computer==0):
                        self.equation.set("You lose!")
                elif(self.unum==-1 and self.computer==1):
                        self.equation.set("You win!")
                elif(self.unum==0 and self.computer==1):
                        self.equation.set("You lose!")
                elif(self.unum==0 and self.computer==-1):
                        self.equation.set("You win!")
                else:
                    self.equation.set("Invalid Input!!")
        

root= Tk()
g = game(root)
root.mainloop()
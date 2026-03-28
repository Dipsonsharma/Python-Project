from tkinter import Tk, Entry, Button, StringVar, Canvas
import random

class game:
    def __init__(self, master):
        master.title("Game")
        master.geometry('370x420+0+0')
        master.config(bg='#d6baa3')

        self.equation = StringVar()
        self.myval = StringVar()
        self.cc = StringVar()

        # Entry fields
        Entry(width=22, bg='#f6efeb', fg='#4d4949', font=('Helvetica',28), textvariable=self.myval).place(x=10,y=30,width=110,height=80)
        Entry(width=22, bg='#f6efeb', fg='#4d4949', font=('Helvetica',28), textvariable=self.cc).place(x=130,y=30,width=110,height=80)
        Entry(width=22, bg='#f6efeb', fg='#4d4949', font=('Helvetica',24), textvariable=self.equation).place(x=250,y=30,width=110,height=40)

        # START button as rounded Canvas
        self.start_canvas = Canvas(master, width=50, height=35, bg='#d6baa3', highlightthickness=0)
        self.start_canvas.place(x=255, y=75)
        self.draw_rounded_button(self.start_canvas, "START", "#117800", self.solve)

        # RESET button as rounded Canvas
        self.reset_canvas = Canvas(master, width=50, height=35, bg='#d6baa3', highlightthickness=0)
        self.reset_canvas.place(x=315, y=75)
        self.draw_rounded_button(self.reset_canvas, "RESET", "#be1010", self.clear)

        # Scissor-Paper-Rock buttons
        Button(width=11,height=4,text='✂️\nScissor',relief='flat',bg='white',font=('Helvetica',24),command=lambda:self.show('scissor')).place(x=10 ,y=160 , width=110, height=250)
        Button(width=11,height=4,text='📄\nPaper',relief='flat',bg='white',font=('Helvetica',24),command=lambda:self.show('paper')).place(x=130,y=160, width=110, height=250 )
        Button(width=11,height=4,text='🪨\nRock',relief='flat',bg='white',font=('Helvetica',24),command=lambda:self.show('rock')).place(x=250,y=160, width=110, height=250)

    # Function to draw rounded rectangle button
    def draw_rounded_button(self, canvas, text, color, command):
        w = int(canvas['width'])
        h = int(canvas['height'])
        r = 10  # corner radius

        # Draw four corner arcs
        canvas.create_arc((0,0,r*2,r*2), start=90, extent=90, fill=color, outline=color)
        canvas.create_arc((w-2*r,0,w,r*2), start=0, extent=90, fill=color, outline=color)
        canvas.create_arc((0,h-2*r,2*r,h), start=180, extent=90, fill=color, outline=color)
        canvas.create_arc((w-2*r,h-2*r,w,h), start=270, extent=90, fill=color, outline=color)

        # Draw rectangles to fill
        canvas.create_rectangle(r, 0, w-r, h, fill=color, outline=color)
        canvas.create_rectangle(0, r, w, h-r, fill=color, outline=color)

        # Draw text
        canvas.create_text(w//2, h//2, text=text, fill='white', font=('Helvetica', 9, 'bold'))

        # Bind click
        canvas.bind("<Button-1>", lambda e: command())

    # Show user choice
    def show(self, value):
        a = str(value).title()
        self.myval.set(a)
        self.v = value

    # Reset fields
    def clear(self):
        self.equation.set('')
        self.myval.set('')
        self.cc.set('')

    # Game logic
    def solve(self):
        self.computer = random.choice([1,-1,0])
        con={"scissor":1, "paper":0, "rock":-1}
        revcon={ 1:"Scissor" , 0:"Paper" , -1:"Rock" }

        # computer choice
        self.cc.set(str(revcon.get(self.computer)))

        # human choice
        self.unum = con.get(self.v)

        if self.unum == self.computer:
            self.equation.set("Draw")
        else:
            if self.unum==1 and self.computer==0:
                self.equation.set("You win!")
            elif self.unum==1 and self.computer==-1:
                self.equation.set("You lose!")
            elif self.unum==-1 and self.computer==0:
                self.equation.set("You lose!")
            elif self.unum==-1 and self.computer==1:
                self.equation.set("You win!")
            elif self.unum==0 and self.computer==1:
                self.equation.set("You lose!")
            elif self.unum==0 and self.computer==-1:
                self.equation.set("You win!")
            else:
                self.equation.set("Invalid Input!!")

root = Tk()
g = game(root)
root.mainloop()

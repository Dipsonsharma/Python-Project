from tkinter import Tk, Entry, StringVar, Canvas
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

        # START button
        self.start_canvas = Canvas(master, width=50, height=35, bg='#d6baa3', highlightthickness=0)
        self.start_canvas.place(x=255, y=75)
        self.draw_rounded_button(self.start_canvas, "START", "#117800", self.solve)

        # RESET button
        self.reset_canvas = Canvas(master, width=50, height=35, bg='#d6baa3', highlightthickness=0)
        self.reset_canvas.place(x=315, y=75)
        self.draw_rounded_button(self.reset_canvas, "RESET", "#be1010", self.clear)

        # Scissor-Paper-Rock buttons
        self.scissor_canvas = Canvas(master, width=110, height=250, bg='#d6baa3', highlightthickness=0)
        self.scissor_canvas.place(x=10, y=160)
        self.draw_rounded_button(self.scissor_canvas, '✂️\nScissor', '#f6efeb', lambda: self.show('scissor'), font_size=24, text_color='#4d4949')

        self.paper_canvas = Canvas(master, width=110, height=250, bg='#d6baa3', highlightthickness=0)
        self.paper_canvas.place(x=130, y=160)
        self.draw_rounded_button(self.paper_canvas, '📄\nPaper', '#f6efeb', lambda: self.show('paper'), font_size=24, text_color='#4d4949')

        self.rock_canvas = Canvas(master, width=110, height=250, bg='#d6baa3', highlightthickness=0)
        self.rock_canvas.place(x=250, y=160)
        self.draw_rounded_button(self.rock_canvas, '🪨\nRock', '#f6efeb', lambda: self.show('rock'), font_size=24, text_color='#4d4949')

    # Draw rounded rectangle button on canvas
    def draw_rounded_button(self, canvas, text, color, command, font_size=10, text_color='white'):
        w = int(canvas['width'])
        h = int(canvas['height'])
        r = 20  # corner radius

        # Four corner arcs
        canvas.create_arc((0,0,r*2,r*2), start=90, extent=90, fill=color, outline=color)
        canvas.create_arc((w-2*r,0,w,r*2), start=0, extent=90, fill=color, outline=color)
        canvas.create_arc((0,h-2*r,2*r,h), start=180, extent=90, fill=color, outline=color)
        canvas.create_arc((w-2*r,h-2*r,w,h), start=270, extent=90, fill=color, outline=color)

        # Center rectangles to fill
        canvas.create_rectangle(r, 0, w-r, h, fill=color, outline=color)
        canvas.create_rectangle(0, r, w, h-r, fill=color, outline=color)

        # Button text
        canvas.create_text(w//2, h//2, text=text, fill=text_color, font=('Helvetica', font_size, 'bold'))

        # Bind click
        canvas.bind("<Button-1>", lambda e: command())

    # Show user choice
    def show(self, value):
        self.myval.set(value.title())
        self.v = value

    # Reset all fields
    def clear(self):
        self.equation.set('')
        self.myval.set('')
        self.cc.set('')

    # Game logic
    def solve(self):
        self.computer = random.choice([1,-1,0])
        con={"scissor":1, "paper":0, "rock":-1}
        revcon={ 1:"Scissor" , 0:"Paper" , -1:"Rock" }

        # Computer choice
        self.cc.set(str(revcon.get(self.computer)))

        # Human choice
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

# Run the game
root = Tk()
g = game(root)
root.mainloop()

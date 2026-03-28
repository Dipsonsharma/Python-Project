from tkinter import Tk, Entry, StringVar, Canvas, Label
import random

class game:
    def __init__(self, master):
        master.title("Game")
        master.geometry('370x420+0+0')
        master.config(bg='#d6baa3')

        self.equation = StringVar()
        self.myval = StringVar()
        self.cc = StringVar()

        # Labels above entry boxes (bigger, bold, ending with ':')
        Label(master, text="YOU CHOSE:", bg='#d6baa3', fg='#4d4949', font=('Helvetica', 12, 'bold')).place(x=20, y=10)
        Label(master, text="COMPUTER CHOSE:", bg='#d6baa3', fg='#4d4949', font=('Helvetica', 12, 'bold')).place(x=130, y=10)
        Label(master, text="RESULT:", bg='#d6baa3', fg='#4d4949', font=('Helvetica', 12, 'bold')).place(x=260, y=10)

        # Rounded entry boxes using Canvas
        self.create_rounded_entry(master, 10, 30, 110, 80, self.myval, font_size=20)
        self.create_rounded_entry(master, 130, 30, 110, 80, self.cc, font_size=20)
        self.create_rounded_entry(master, 250, 30, 110, 40, self.equation, font_size=16)

        # START button
        self.start_canvas = Canvas(master, width=50, height=35, bg='#d6baa3', highlightthickness=0)
        self.start_canvas.place(x=255, y=75)
        self.draw_rounded_button(self.start_canvas, "START", "#117800", self.solve, 'white')

        # RESET button
        self.reset_canvas = Canvas(master, width=50, height=35, bg='#d6baa3', highlightthickness=0)
        self.reset_canvas.place(x=315, y=75)
        self.draw_rounded_button(self.reset_canvas, "RESET", "#be1010", self.clear, 'white')

        # Scissor-Paper-Rock buttons
        self.scissor_canvas = Canvas(master, width=110, height=250, bg='#d6baa3', highlightthickness=0)
        self.scissor_canvas.place(x=10, y=160)
        self.draw_emoji_button(self.scissor_canvas, '✂️', 'Scissor', '#f6efeb', lambda: self.show('scissor✂️'))

        self.paper_canvas = Canvas(master, width=110, height=250, bg='#d6baa3', highlightthickness=0)
        self.paper_canvas.place(x=130, y=160)
        self.draw_emoji_button(self.paper_canvas, '📄', 'Paper', '#f6efeb', lambda: self.show('paper📄'))

        self.rock_canvas = Canvas(master, width=110, height=250, bg='#d6baa3', highlightthickness=0)
        self.rock_canvas.place(x=250, y=160)
        self.draw_emoji_button(self.rock_canvas, '🪨', 'Rock', '#f6efeb', lambda: self.show('rock🪨'))

    # Function to create rounded entry boxes
    def create_rounded_entry(self, master, x, y, width, height, text_var, font_size=28):
        r = 20  # corner radius
        canvas = Canvas(master, width=width, height=height, bg='#d6baa3', highlightthickness=0)
        canvas.place(x=x, y=y)

        # Draw rounded rectangle
        canvas.create_arc((0,0,r*2,r*2), start=90, extent=90, fill='#f6efeb', outline='#f6efeb')
        canvas.create_arc((width-2*r,0,width,r*2), start=0, extent=90, fill='#f6efeb', outline='#f6efeb')
        canvas.create_arc((0,height-2*r,2*r,height), start=180, extent=90, fill='#f6efeb', outline='#f6efeb')
        canvas.create_arc((width-2*r,height-2*r,width,height), start=270, extent=90, fill='#f6efeb', outline='#f6efeb')
        canvas.create_rectangle(r,0,width-r,height, fill='#f6efeb', outline='#f6efeb')
        canvas.create_rectangle(0,r,width,height-r, fill='#f6efeb', outline='#f6efeb')

        # Place Entry on top (borderless, Helvetica)
        entry = Entry(master, bg='#f6efeb', fg='#4d4949', font=('Helvetica', font_size),
                      textvariable=text_var, relief='flat', bd=0, highlightthickness=0, justify='center')
        entry.place(x=x+5, y=y+5, width=width-10, height=height-10)

    # Rounded button for START/RESET
    def draw_rounded_button(self, canvas, text, color, command, text_color='white', font_size=10):
        w = int(canvas['width'])
        h = int(canvas['height'])
        r = 10

        canvas.create_arc((0,0,r*2,r*2), start=90, extent=90, fill=color, outline=color)
        canvas.create_arc((w-2*r,0,w,r*2), start=0, extent=90, fill=color, outline=color)
        canvas.create_arc((0,h-2*r,2*r,h), start=180, extent=90, fill=color, outline=color)
        canvas.create_arc((w-2*r,h-2*r,w,h), start=270, extent=90, fill=color, outline=color)
        canvas.create_rectangle(r,0,w-r,h, fill=color, outline=color)
        canvas.create_rectangle(0,r,w,h-r, fill=color, outline=color)
        canvas.create_text(w//2, h//2, text=text, fill=text_color, font=('Helvetica', font_size, 'bold'))
        canvas.bind("<Button-1>", lambda e: command())

    # Rounded button with emoji above text
    def draw_emoji_button(self, canvas, emoji, text, color, command, emoji_size=50, text_color='#4d4949'):
        w = int(canvas['width'])
        h = int(canvas['height'])
        r = 20
        canvas.create_arc((0,0,r*2,r*2), start=90, extent=90, fill=color, outline=color)
        canvas.create_arc((w-2*r,0,w,r*2), start=0, extent=90, fill=color, outline=color)
        canvas.create_arc((0,h-2*r,2*r,h), start=180, extent=90, fill=color, outline=color)
        canvas.create_arc((w-2*r,h-2*r,w,h), start=270, extent=90, fill=color, outline=color)
        canvas.create_rectangle(r,0,w-r,h, fill=color, outline=color)
        canvas.create_rectangle(0,r,w,h-r, fill=color, outline=color)
        canvas.create_text(w//2, h//3, text=emoji, font=('Helvetica', emoji_size))
        canvas.create_text(w//2, h*2//3 + 10, text=text, font=('Helvetica', 24, 'bold'), fill=text_color)
        canvas.bind("<Button-1>", lambda e: command())

    # Show user choice
    def show(self, value):
        self.myval.set(value.title())
        self.v = value

    # Clear
    def clear(self):
        self.equation.set('')
        self.myval.set('')
        self.cc.set('')

    # Game logic
    def solve(self):
        self.computer = random.choice([1,-1,0])
        con={"scissor✂️":1, "paper📄":0, "rock🪨":-1}
        revcon={ 1:"Scissor✂️" , 0:"Paper📄" , -1:"Rock🪨" }

        self.cc.set(str(revcon.get(self.computer)))
        self.unum = con.get(self.v)

        if self.unum == self.computer:
            self.equation.set("Draw😑!")
        else:
            if self.unum==1 and self.computer==0:
                self.equation.set("You Won🥳!")
            elif self.unum==1 and self.computer==-1:
                self.equation.set("You Lose☹️!")
            elif self.unum==-1 and self.computer==0:
                self.equation.set("You Lose☹️!")
            elif self.unum==-1 and self.computer==1:
                self.equation.set("You Won🥳!")
            elif self.unum==0 and self.computer==1:
                self.equation.set("You Lose☹️!")
            elif self.unum==0 and self.computer==-1:
                self.equation.set("You Won🥳!")
            else:
                self.equation.set("Invalid Input!!")

# Run the game
root = Tk()
g = game(root)
root.mainloop()

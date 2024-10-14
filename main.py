import tkinter
import random

colours = ['Red', 'Yellow', 'Orange', 'Pink', 'Green', 'Blue', 'Violet', 'White', 'Black', 'Brown', 'Indigo', 'Purple']
score = 0
timeleft = 60

def startGame(event):
    global timeleft
    if timeleft == 60:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scorelabel.config(text="Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text="Time left: " + str(timeleft))
        timelabel.after(1000, countdown)

root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")

instructions = tkinter.Label(root, text="Type in the colour of the words, not the word text!", font=('Helvetica', 12))
instructions.pack()

scorelabel = tkinter.Label(root, text="Press Enter to start", font=('Helvetica', 12))
scorelabel.pack()

timelabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timelabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
e.pack()
e.focus_set()

root.bind('<Return>', startGame)

root.mainloop()

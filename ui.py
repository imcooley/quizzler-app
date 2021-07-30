from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.mainloop()

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=1)

        check_image = PhotoImage(file="images/true.png")
        self.known_button = Button(image=check_image, highlightthickness=0)
        self.known_button.grid(row=2, column=0)

        cross_image = PhotoImage(file="images/false.png")
        self.unknown_button = Button(image=cross_image, highlightthickness=0)
        self.unknown_button.grid(row=2, column=1)
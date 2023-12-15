from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"


class FlashCardApp:
    def __init__(self, window, data):
        self.window = window
        self.window.title("Flash Cards")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.flipping = None

        self.canvas = Canvas(width=800, height=526)
        self.card_front_img = PhotoImage(file="./images/card_front.png")
        self.card_back_img = PhotoImage(file="./images/card_back.png")
        self.canvas_image = self.canvas.create_image(
            400, 263, image=self.card_front_img)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_title = self.canvas.create_text(
            400, 150, text="", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(
            400, 263, text="", font=("Ariel", 60, "bold"))

        self.cross_image = PhotoImage(file="./images/wrong.png")
        self.unknown_button = Button(
            image=self.cross_image, highlightthickness=0, command=self.next_card)
        self.unknown_button.grid(row=1, column=0)

        self.check_image = PhotoImage(file="./images/right.png")
        self.check_button = Button(
            image=self.check_image, highlightthickness=0, command=self.next_card)
        self.check_button.grid(row=1, column=1)

        self.to_learn = data.to_dict(orient="records")
        self.current_card = {}
        self.current_side = "German"

        self.default_card()  

        self.next_card()
        self.continuous_flip()


    def default_card(self):
         if not self.current_card:
        # If self.current_card is empty, choose a random card
            self.current_card = random.choice(self.to_learn)

         self.canvas.itemconfig(self.card_title, text="German")
         self.canvas.itemconfig(self.card_word, text=self.current_card["German"])
         self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
         self.current_side = "German"    
         self.window.after(3000, self.continuous_flip)

    def continuous_flip(self):
        self.flip_card()
        self.flipping = self.window.after(3000, self.continuous_flip)
       

    def next_card(self):
        
        if self.flipping:
            self.window.after_cancel(self.flipping)
        self.current_card = random.choice(self.to_learn)
        self.canvas.itemconfig(self.card_title, text="German")
        self.canvas.itemconfig(self.card_word, text=self.current_card["German"])
        self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
        self.flipping = self.window.after(3000, self.continuous_flip)

        
        

    def flip_card(self):
        
        if self.current_side == "German":
            self.canvas.itemconfig(self.card_title, text="German")
            self.canvas.itemconfig(self.card_word, text=self.current_card["German"])
            self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
            self.current_side = "English"
        else:
            self.canvas.itemconfig(self.card_title, text="English")
            self.canvas.itemconfig(self.card_word, text=self.current_card["English"])
            self.canvas.itemconfig(self.canvas_image, image=self.card_back_img)
            self.current_side = "German"
    
 
data = pandas.read_csv("./data/flash_card_project - Sheet1.csv")
window = Tk()


flash_card_app = FlashCardApp(window, data)
window.mainloop()

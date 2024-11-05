import time
from tkinter import *
from pandas import read_csv, DataFrame
import random
BACKGROUND_COLOR = "#B1DDC6"
# read data:
try:
    data = read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}


def generate_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(list(to_learn))
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(title_text, text=f"French", fill="black")
    canvas.itemconfig(card_background, image=img_card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=img_card_back)


def is_known():
    to_learn.remove(current_card)
    generate_random_word()
    data2 = DataFrame(to_learn)
    data2.to_csv("data/words_to_learn.csv", index=False)

#  UI:
# window:
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
#Canvas:
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_card_front = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image=img_card_front)
canvas.grid(column=0, row=0, columnspan=2)
img_card_back = PhotoImage(file="./images/card_back.png")
# canvas text:
title_text = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
# right button:
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=2)
# wrong button:
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_random_word)
wrong_button.grid(column=0, row=2)

generate_random_word()
window.mainloop()

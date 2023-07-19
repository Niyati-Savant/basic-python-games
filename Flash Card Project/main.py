from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
word_list = {}
try:
    word_frame = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    all_words_frame = pandas.read_csv("./data/french_words.csv")
    word_list = all_words_frame.to_dict(orient="records")
else:
    word_list = word_frame.to_dict(orient="records")

def next_card():
    global current_word
    current_word = choice(word_list)
    french_word = current_word["French"]
    canvas.itemconfig(flash_card, image=front_img)
    canvas.itemconfig(lang_text, text="French",fill="black")
    canvas.itemconfig(word_text, text=french_word,fill="black")
    screen.after(3000, func=flip_card)


def flip_card():
    global current_word,flip_timer
    screen.after_cancel(flip_timer)
    canvas.itemconfig(flash_card, image=back_img)
    canvas.itemconfig(lang_text, text="English",fill="white")
    canvas.itemconfig(word_text, text=current_word["English"],fill="white")
    flip_timer = screen.after(3000, func=flip_card)

def know_word():
    global current_word
    word_list.remove(current_word)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv",index=False)
    # with open(file="words_to_learn.csv",mode='w') as file:

    next_card()




screen = Tk()
screen.title("Learn French")
screen.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = screen.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
flash_card = canvas.create_image(400, 263, image=front_img)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
lang_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 250, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

dont_know_img = PhotoImage(file="./images/wrong.png")
dont_know = Button(image=dont_know_img, command=next_card, highlightthickness=0)
dont_know.grid(row=1, column=0)

show_ans_img = PhotoImage(file="./images/right.png")
show_ans = Button(image=show_ans_img, command=know_word, highlightthickness=0)
show_ans.grid(row=1, column=1)

next_card()

screen.mainloop()

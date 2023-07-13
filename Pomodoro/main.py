from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_call():
    global  reps
    reps = 0
    screen.after_cancel(timer)
    timer_label.config(text="TIMER",fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="LONG BREAK",fg=PINK)
        count_down(long_break_sec)
        screen.attributes('-topmost', 1)
        screen.attributes('-topmost', 0)
    elif reps % 2 == 0:
        timer_label.config(text="SHORT BREAK",fg=GREEN)
        count_down(short_break_sec)
        screen.attributes('-topmost', 1)
        screen.attributes('-topmost', 0)
    else :
        timer_label.config(text="WORK",fg=RED)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = screen.after(100, count_down, count - 1)
    else:
        timer_start()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


screen = Tk()
screen.title("Pomodoro", )
screen.config(pady=50, padx=100, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

img_bg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img_bg, )
canvas.grid(row=1, column=1)

timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start = Button(text="Start", command=timer_start, highlightthickness=0)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=reset_call, highlightthickness=0)
reset.grid(row=2, column=2)

checkmark = Label( fg=GREEN, highlightthickness=0)
checkmark.grid(row=3, column=1)

screen.mainloop()

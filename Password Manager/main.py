from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_letters = [choice(letters) for _ in range(randint(5, 8))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbol
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_content():
    website_name = website_entry.get()
    mail_entered = email_entry.get()
    password = pass_entry.get()

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please Don't leave any empty fields")

    else:
        is_okay = messagebox.askokcancel(title=f"Website: {website_name}",
                                         message=f"Should I save the following:\n "
                                                 f"Email: {mail_entered} \n Password: {password}")
        if is_okay:
            with open(file="Password_details", mode='a') as data:
                data.write(f"\n {website_name} || {mail_entered}  || {password} ")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=20)
logo_img = PhotoImage(file="title_logo.png")
screen.iconphoto(False, logo_img)

canvas = Canvas(width=200, height=200)
bg_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "dummy@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

gen_pass = Button(text="Generate Password", command=generate_pass)
gen_pass.grid(row=3, column=2)

add = Button(text="Add", width=36, command=add_content, background="green", foreground="white")
add.grid(row=4, column=1, columnspan=2)

screen.mainloop()

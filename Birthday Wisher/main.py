import datetime as dt
import smtplib
import pandas
import random
# random.choice("letter_1.txt", "letter_2.txt", "letter_3.txt")
# Your mail and app-password not official password
my_mail = ""
password = ""

now = dt.datetime.now()
current_day = now.date().day
current_month = now.date().month
letter_list = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
with open("birthdays.csv") as file:
    birthday_data = pandas.read_csv(file)
    birth_dict = birthday_data.to_dict(orient="records")

for people in birth_dict:
    if current_day == people['day'] and current_month == people['month']:
        print(f"Yes! Its {people['name']}'s Birthday")
        letter = random.choice(letter_list)
        with open(file=letter,mode='r') as wish_letter:
            contents = wish_letter.read()
            contents = contents.replace("[NAME]", people['name'])
            print(contents)
        # In case you're not using gmail,google your Smtp
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail,password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs=people["email"],
                                msg=f"Subject:Happy Birthday \n\n {contents}")



# 4. Send the letter generated in step 3 to that person's email address.

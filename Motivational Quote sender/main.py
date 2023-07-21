import smtplib
import random
import datetime as dt

#add your password and sender's mail (passord is found using Google's Security) as well as receiver mail
my_mail = ""
password = ""
sender_mail = ""
with open("quotes.txt", mode="r") as file:
    quote_list = file.readlines()

now = dt.datetime.now()
day = now.weekday()

# if u r not using gmail ,just google your smtp and add it in the brackets
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # for a secure connection
    msg = random.choice(quote_list)
    if day == 4:
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=sender_mail,
            msg=f"Subject:Motivational Message \n\n {msg}"
        )

import requests
from datetime import datetime
import smtplib

MY_LAT = 19.047321
MY_LNG = 73.069908

my_mail = ""
password = ""
sender_mail = ""


def loc_check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]
    iss_latitude = float(data['latitude'])
    iss_longitude = float(data['longitude'])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG + 5 <= iss_longitude <= MY_LNG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data['results']["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.now().hour
    if current_time >= sunset or current_time <= sunrise:
        return True

wh
if loc_check() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # for a secure connection
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=sender_mail,
            msg=f"Subject:Look Up! \n\n The ISIS is above you in the sky"
        )
import requests
import json
from twilio.rest import Client

# Weather.json has sample data
# Get weather Api from https://api.openweathermap.org and auth_token and SID from Twilio
# BOTH NEED FREE REGISTRATIONS
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "YOUR API"
account_sid = 'YOUR ACCOUNT ID (TWILIO)'
auth_token = 'YOUR AUTH TOKEN (TWILIO)'

#GET LATITUDE AND LONGITUDE OF YOUR AREA FROM https://www.latlong.net/
weather_params = {
    "lat": -1.285790,
    "lon": 36.820030,
    "exclude" : "current,minutely,daily",
    "appid" : api_key
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(json.dumps(weather_data, indent=4))
need = weather_data['hourly'][:12]
list_conditions = []
for hr in need:
    X = hr['weather'][0]['id']
    list_conditions.append(X)

will_rain = False

for code in list_conditions:
    if int(code) < 700:
        will_rain = True
print(list_conditions)
if will_rain == True :
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_='TWILIO PHONE NUMBER',
      body="Don't Forget to carry an Umbrella",
      to='YOUR ACTUAL PHONE NUMBER'
    )
    print(message.sid)
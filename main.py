import requests
from twilio.rest import Client

api_key = "API KEY"
account_sid = "ACCOUNT ID"
auth_token = "YOUR AUTH TOKEN"

parameters = {
    "lat": YOUR COORDINATES,
    "lon": YOUR COORDINATES,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
sliced_data = weather_data["hourly"][:12]    # sliced a list of 12 hours data

will_rain = False

for hour_data in sliced_data:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella ☔.",
        from_='DEMO',
        to='YOUR NUMBER'
    )

    print(message.status)

import requests
from twilio.rest import Client

OpenWeather_Endpoint = "ENTER WEATHER API END POINT HERE"
api_key = "ENTER WEATHER API KEY HERE"

account_sid = "ENTER TWILIO SID HERE"
auth_token = "ENTER TWILIO AUTH TOKEN HERE"


weather_params = {
    "lat":  33.5651,
    "lon": 73.0169,
    "appid": api_key,
}

response = requests.get(OpenWeather_Endpoint, params=weather_params)
response.raise_for_status()
print("http status response code:")
print(response.status_code)

# Weather Data Code Reference: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
weather_data = response.json()
print("Weather Data Code:")
print(weather_data["weather"][0]["id"])


# Get the weather condition code
# weather_condition_code = weather_data["weather"][0]["id"]
weather_condition_code = 23

will_rain = False
if weather_condition_code < 700:  # Check if the weather condition code indicates rain
    will_rain = True
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Message Text Goes here..",
        from_="ENTER TWILIO PROVIDED NUMBER",
        to="ENTER YOUR REGISTERED TWILIO NUMBER",
    )
    print("Message Status: " + message.status)


import requests
from datetime import datetime

MY_LAT = 24.713552
MY_LONG = 46.675297

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

is_latitude = float(data["iss_position"]["latitude"])
is_longitude = float(data["iss_position"]["longitude"])

def current_position():
    c_lat = MY_LAT - is_latitude
    c_lng = MY_LONG - is_latitude

    if (5 > c_lat > -5 ) and (5 > c_lng > -5):
        return True
    else:
        return False

print(current_position())
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0
# }

# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

# response.raise_for_status()

# data = response.json()
# sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
# sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

# time_now = datetime.now()


import requests
from datetime import datetime
import smtplib

MY_LAT = 24.713552
MY_LONG = 46.675297

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    is_latitude = float(data["iss_position"]["latitude"])
    is_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT + 5 > is_latitude > MY_LAT - 5 ) and (MY_LONG + 5 > is_longitude > MY_LONG - 5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


def main():

    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="hassanwebdevt@gmail.com", password="password")
            connection.sendmail(
                from_addr="hassanwebdevt@gmail.com",
                to_addrs="elwany_hassan@hotmail.com",
                msg=f"Subject: subject\n\n it's night and match cords look up"
            )

if __name__ == "__main__":
    main()
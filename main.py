import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = 'email_example@gmail.com'
MY_PASSWORD = 'password_123(-)abc_example'

MY_LAT = 48.669102
MY_LONG = 12.690720

def is_iss_overhead():
    iss_response = requests.get(
        url="http://api.open-notify.org/iss-now.json",
        timeout=10
    )
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data['iss_position']['latitude'])
    iss_longitude = float(iss_data['iss_position']['longitude'])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }

    ss_response = requests.get(
        url='https://api.sunrise-sunset.org/json',
        params=parameters,
        timeout=10
    )
    ss_response.raise_for_status()
    ss_data = ss_response.json()

    sunrise = int(ss_data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(ss_data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = dt.datetime.now(dt.timezone.utc).hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg='Subject: ISS Overhead Alert!\n\n'
                    'The ISS is currently above your location.\n'
                    'Go outside and take a look!'
            )

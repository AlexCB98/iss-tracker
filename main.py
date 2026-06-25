import requests
import datetime as dt

MY_LAT = 48.669102
MY_LONG = 12.690720

iss_response = requests.get(
    url="http://api.open-notify.org/iss-now.json",
    timeout=10
)
iss_response.raise_for_status()
iss_data = iss_response.json()

iss_latitude = float(iss_data['iss_position']['latitude'])
iss_longitude = float(iss_data['iss_position']['longitude'])

iss_position = (iss_latitude, iss_longitude)

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}

ss_response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
ss_response.raise_for_status()
ss_data = ss_response.json()

sunrise = int(ss_data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(ss_data['results']['sunset'].split('T')[1].split(':')[0])

time_now = dt.datetime.now()


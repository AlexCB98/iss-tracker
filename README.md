# ISS Overhead Notifier

A simple Python project that checks whether the International Space Station (ISS) is currently overhead during the night and sends an email notification.

This project was built using Python, public APIs, and SMTP.

---

## Features

* Retrieves the current ISS location
* Retrieves local sunrise and sunset times
* Checks if the ISS is near your location
* Checks if it is currently night
* Sends an email notification when both conditions are met

---

## What I practiced

* Working with multiple APIs
* Sending HTTP requests with `requests`
* Reading and processing JSON data
* Working with functions
* Using `datetime` and `time`
* Sending emails with `smtplib`
* Combining multiple conditions into a complete application

---

## Project structure

```

main.py

```

---

## How to run

Run the project with:

```bash

python main.py

```

---

## Technologies used

* Python
* Requests
* JSON
* Datetime
* Time
* SMTP

---

## Note

This project combines multiple concepts learned throughout the course, including APIs, JSON data, time handling, and email automation. It periodically checks the ISS position and sends an email notification when the station is overhead during the night.

---

## Author

Alex — Aspiring Python developer building projects step by step through daily practice, with the long-term goal of becoming a professional software developer.

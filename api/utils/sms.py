import requests

EBULKSMS_URL = "https://api.ebulksms.com/sendsms.json"
SENDER = ""
API_KEY = ""
USERNAME = ""

def send_otp(phone_number, otp):
    payload = {
        "SMS": {
            "auth": {
                "username": USERNAME,
                "apikey": API_KEY
            },
            "message": {
                "sender": SENDER,
                "messagetext": f"Your OTP is {otp}",
                "flash": "0"
            },
            "recipients": {
                "gsm": [{"msidn": phone_number}]
            }
        }
    }

    res = requests.post(EBULKSMS_URL, json=payload)
    return res.status_code, res.json()

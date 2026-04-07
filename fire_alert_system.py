# ==============================
# 🔥 SMART FIRE ALERT SYSTEM
# ==============================

from twilio.rest import Client
import random
import time
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# ==============================
# 🔐 TWILIO CONFIG
# ==============================
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

TO_NUMBER = "whatsapp:+91XXXXXXXXXX"
FROM_NUMBER = "whatsapp:+14155238886"

# ==============================
# 📍 LOCATION (Chennai example)
# ==============================
LAT = 13.0827
LON = 80.2707

maps_link = f"https://www.google.com/maps?q={LAT},{LON}"

# ==============================
# 🧠 TRAIN SIMPLE ML MODEL
# ==============================

# Sample training data [temp, smoke, gas]
X = [
    [30, 100, 200],   # safe
    [35, 150, 300],   # safe
    [60, 400, 600],   # fire
    [70, 500, 700],   # fire
    [55, 350, 500],   # fire
    [40, 200, 300]    # safe
]

y = [0, 0, 1, 1, 1, 0]

model = RandomForestClassifier()
model.fit(X, y)

# ==============================
# 📲 SEND WHATSAPP ALERT
# ==============================

def send_alert():
    message_body = f"""
🔥 FIRE ALERT!

📍 Location: {maps_link}

⚠️ Fire detected. Please evacuate immediately!

தமிழில்:
🔥 தீ விபத்து கண்டறியப்பட்டது!
உடனே வெளியேறவும்!
"""

    message = client.messages.create(
        from_=FROM_NUMBER,
        body=message_body,
        to=TO_NUMBER
    )

    print("Alert Sent:", message.sid)

# ==============================
# 🔍 SENSOR SIMULATION
# ==============================

def get_sensor_values():
    temperature = random.randint(25, 80)
    smoke = random.randint(50, 600)
    gas = random.randint(100, 800)
    return temperature, smoke, gas

# ==============================
# 🧠 FIRE DETECTION LOGIC
# ==============================

def detect_fire(temp, smoke, gas):

    # Rule-based check
    if smoke > 300 and temp > 50:
        rule_result = True
    else:
        rule_result = False

    # ML prediction
    prediction = model.predict([[temp, smoke, gas]])[0]

    if rule_result and prediction == 1:
        return True
    return False

# ==============================
# 🔁 MAIN LOOP
# ==============================

while True:
    temp, smoke, gas = get_sensor_values()

    print(f"\nTemp: {temp}°C | Smoke: {smoke} | Gas: {gas}")

    if detect_fire(temp, smoke, gas):
        print("🔥 FIRE DETECTED!")
        send_alert()
        break
    else:
        print("✅ Safe")

    time.sleep(1)

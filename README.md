# 🔥 Smart Fire Alert System
🚨 Intelligent fire detection system with real-time alerts

---

## 🧠 Overview

This project is a smart fire alert system designed to reduce false alarms using a combination of multi-sensor data and intelligent decision-making.

Unlike traditional systems, it verifies conditions before triggering alerts, making it more reliable and practical.

---

## 🚀 Features

- 🔍 Multi-sensor simulation (Temperature, Smoke, Gas)
- 🧠 Hybrid detection (Rule-based + Machine Learning)
- 📉 Reduced false alarms
- 📲 Real-time alert using Twilio (WhatsApp/SMS)
- 📍 Location sharing via Google Maps
- 🌐 Bilingual alert (English + Tamil)

---

## ⚙️ Tech Stack

- Python
- Machine Learning (Random Forest - scikit-learn)
- Twilio API
- NumPy

---

## 🔄 How It Works

1. Sensor values are generated (simulated)
2. Rule-based logic checks initial conditions
3. Machine learning model validates the result
4. If confirmed:
   - Fire alert is triggered
   - Message is sent with location

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/smart-fire-alert-system.git
cd smart-fire-alert-system

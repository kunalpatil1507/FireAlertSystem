from datetime import datetime
from .firebase_config import ref

def push_to_firebase(temperature, smoke, fire_detected, alert_message):
    """Push sensor data + alert to Firebase Realtime Database"""
    data = {
        "temperature": temperature,
        "smoke": smoke,
        "fire_detected": fire_detected,
        "alert": alert_message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    ref.push(data)
    print("✅ Data pushed to Firebase")

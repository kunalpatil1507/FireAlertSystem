import serial
import requests
import time

# 🔹 Update these:
SERIAL_PORT = "COM3"    # Change COM port (Windows: COM3, COM4... | Linux: /dev/ttyUSB0)
BAUD_RATE = 9600
FIREBASE_URL = "https://console.firebase.google.com/u/0/project/fireandsmoke-5a5b6/database/fireandsmoke-5a5b6-default-rtdb/data/~2F?fb_gclid=CjwKCAjwobnGBhBNEiwAu2mpFHxGhvYcRZjW7EiyKNgCH0_pxHz7FsFPQnFTIAQwPUwRYRF5vcQKohoCOKoQAvD_BwE"

# Open serial connection to Arduino
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)

while True:
    try:
        line = ser.readline().decode().strip()
        if line:
            parts = line.split(",")
            if len(parts) == 3:  # temperature, smoke, fire
                temp = float(parts[0])
                smoke = int(parts[1])
                fire = parts[2].lower() in ["true", "1", "high"]  # interpret fire as boolean

                data = {"temperature": temp, "smoke": smoke, "fire": fire}

                # Update current values
                requests.put(f"{FIREBASE_URL}/sensor.json", json=data)
                # Append to logs
                requests.post(f"{FIREBASE_URL}/logs.json", json=data)

                print("✅ Sent to Firebase:", data)

        time.sleep(2)

    except Exception as e:
        print("⚠️ Error:", e)
        time.sleep(5)

# Fire and Smoke Alert System 🔥💨

An **IoT + Python based real-time fire and smoke alert system** that monitors temperature and smoke levels, visualizes data, and sends alerts to **ThingSpeak** and **Firebase Realtime Database**. Ideal for homes, offices, and industrial safety monitoring.

---

## Features

- Real-time monitoring of temperature and smoke levels.
- Detects fire risk and alerts users instantly.
- Pushes data to **ThingSpeak** for visualization.
- Stores readings in **Firebase Realtime Database** for historical tracking.
- Graphical visualization of sensor readings.
- Configurable API keys and Firebase credentials using `.env` for security.

---

## Table of Contents

1. [Installation](#installation)  
2. [Usage](#usage)  
3. [Project Structure](#project-structure)  
4. [Environment Variables](#environment-variables)  
5. [Contributing](#contributing)  
6. [License](#license)  

---

## Installation

1. Clone the repository:

``bash
git clone https://github.com/your-username/FireAlertSystem.git
cd FireAlertSystem
Create a virtual environment:

bash
Copy code
python -m venv myvenv
Activate the environment:

Windows (PowerShell):

bash
Copy code
myvenv\Scripts\Activate.ps1
Windows (CMD):

bash
Copy code
myvenv\Scripts\activate.bat
Linux / macOS:

bash
Copy code
source myvenv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Configure your .env file with your API keys:

ini
Copy code
THINGSPEAK_API_KEY=<your_thingspeak_api_key>
FIREBASE_DB_URL=<your_firebase_database_url>
FIREBASE_JSON_PATH=<path_to_your_firebase_json>
Run the system:

bash
Copy code
python main.py
The system will:

Read temperature and smoke sensor data.

Check for fire conditions.

Send data to ThingSpeak.

Push data to Firebase Realtime Database.

Display live readings in the console and graphs.

Project Structure
bash
Copy code
FireAlertSystem/
│
├─ cloud/
│  ├─ firebase_config.py       # Firebase setup
│  ├─ firebase_push.py         # Push data to Firebase
│  └─ thingspeak.py            # Push data to ThingSpeak
│
├─ sensors/
│  └─ get_sensor_data.py       # Simulated or real sensor readings
│
├─ fire_logic/
│  └─ check_fire.py            # Logic to detect fire risk
│
├─ visualization/
│  └─ plot_graph.py            # Graphical visualization of readings
│
├─ main.py                     # Entry point
├─ requirements.txt            # Python dependencies
└─ .env                        # API keys (ignored by git)
Environment Variables
THINGSPEAK_API_KEY – ThingSpeak write API key.

FIREBASE_DB_URL – Firebase Realtime Database URL.

FIREBASE_JSON_PATH – Local path to Firebase service account JSON (not committed to GitHub).

Make sure .env and JSON files are added to .gitignore to prevent exposing secrets.

Contributing
Fork the repository

Create a new branch (git checkout -b feature-name)

Make your changes

Commit your changes (git commit -m "Add feature")

Push to the branch (git push origin feature-name)

Open a pull request

License
This project is licensed under the MIT License. See the LICENSE file for details.

Screenshot / Preview

Simulated visualization of temperature and smoke readings over time.

References
ThingSpeak API

Firebase Admin SDK

Python matplotlib

yaml
Copy code

---

I can also **create a smaller version optimized for GitHub with badges, live demo links, and API documentation** if you want it to look more professional and interactive.  

Do you want me to do that?






<img width="1920" height="1200" alt="Screenshot 2025-09-27 210204" src="https://github.com/user-attachments/assets/3da1f1c2-5b1a-45a0-b177-e6d329ad6744" />
<img width="1920" height="1200" alt="Screenshot 2025-09-27 210143" src="https://github.com/user-attachments/assets/9e46633c-1062-4b29-9bcb-087395d3b337" />

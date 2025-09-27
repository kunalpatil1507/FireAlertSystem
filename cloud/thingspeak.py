import requests
from dotenv import load_dotenv
import os

load_dotenv()
THINGSPEAK_API_KEY = os.getenv("THINGSPEAK_API_KEY")

def send_to_thingspeak(temperature, smoke):
    url = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}&field1={temperature}&field2={smoke}"
    response = requests.get(url)
    return response.status_code

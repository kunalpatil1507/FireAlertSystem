import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os

load_dotenv()
FIREBASE_DB_URL = os.getenv("FIREBASE_DB_URL")

cred = credentials.Certificate("fireandsmoke-5a5b6-firebase-adminsdk-fbsvc-b58502c735.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": FIREBASE_DB_URL
})

ref = db.reference("FireAlertSystem")

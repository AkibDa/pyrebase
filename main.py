import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="gcloud")

import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}

try:
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    auth = firebase.auth()
    storage = firebase.storage()
except Exception as e:
    print(f"❌ Firebase initialization failed: {str(e)}")
    exit(1)

# Login
try:
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user = auth.sign_in_with_email_and_password(email, password)
    print("✅ Successfully logged in!")
except Exception as e:
    print(f"❌ Login failed: {str(e)}")

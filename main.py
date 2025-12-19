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
def login():
  try:
      email = input("Enter your email: ")
      password = input("Enter your password: ")
      user = auth.sign_in_with_email_and_password(email, password)
      print("✅ Successfully logged in!")
  except Exception as e:
      print(f"❌ Login failed: {str(e)}")

# SignUp
def signup():
  try:
      email = input("Enter your email for signup: ")
      password = input("Enter your password for signup: ")
      conf_password = input("Confirm your password: ")
      if password != conf_password:
          raise ValueError("Passwords do not match.")
      try:
        user = auth.create_user_with_email_and_password(email, password)
        print("✅ Successfully signed up!")
      except:
        raise ValueError("Failed to create user. The email might already be in use or the password is too weak.")

  except Exception as e:
      print(f"❌ Signup failed: {str(e)}")

# Main function
if __name__ == "__main__":
    ch = input("Do you want to (l)ogin or (s)ignup? ").lower()
    if ch == 'l':
        login()
    elif ch == 's':
        signup()
    else:
        print("❌ Invalid choice. Please enter 'l' for login or 's' for signup.")

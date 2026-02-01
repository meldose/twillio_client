import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
VERIFY_SID = os.getenv("TWILIO_VERIFY_SERVICE_SID")
PHONE = os.getenv("VERIFY_PHONE_NUMBER")

if not all([ACCOUNT_SID, AUTH_TOKEN, VERIFY_SID, PHONE]):
    raise RuntimeError("Missing required environment variables")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

code = input("Enter verification code: ").strip()

check = client.verify.v2.services(VERIFY_SID) \
    .verification_checks \
    .create(to=PHONE, code=code)

print("Verification result:", check.status)  # approved or pending

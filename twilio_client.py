import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TO_NUMBER = os.getenv("TWILIO_TO_NUMBER")

if not all([ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER, TO_NUMBER]):
    raise RuntimeError("Missing required Twilio environment variables")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


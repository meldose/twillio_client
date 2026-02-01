from twilio_client import client, FROM_NUMBER, TO_NUMBER

message = client.messages.create(
    body="Hello from .env-powered client",
    from_=FROM_NUMBER,
    to=TO_NUMBER
)

print("Message SID:", message.sid)


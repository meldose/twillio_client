from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

# Handle inbound SMS
@app.route("/sms", methods=["POST"])
def sms_reply():
    incoming_msg = request.form.get("Body", "")

    resp = MessagingResponse()
    resp.message(f"You said: {incoming_msg}")

    return Response(str(resp), mimetype="text/xml")


# Handle inbound voice calls
@app.route("/call", methods=["POST"])
def voice_reply():
    resp = VoiceResponse()
    resp.say("Hello! This is your Twilio Python server.")

    return Response(str(resp), mimetype="text/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


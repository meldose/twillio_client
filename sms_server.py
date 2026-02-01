from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms_webhook():
    from_number = request.form.get("From")
    to_number = request.form.get("To")
    body = request.form.get("Body")

    print("=== Incoming SMS ===")
    print("From:", from_number)
    print("To:", to_number)
    print("Body:", body)

    # Optional reply
    resp = MessagingResponse()
    resp.message("SMS received")

    return Response(str(resp), mimetype="application/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


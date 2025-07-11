
import os
from flask import Flask, request, jsonify
import json

# Create a new Flask web app
app = Flask(__name__)

# This will store the incoming messages temporarily
messages = []

# Webhook endpoint
@app.route("/webhook", methods=["POST"])
def webhook():
    # Get the data from LINE's request
    data = request.json

    # Log the received data (for debugging purposes)
    print(json.dumps(data, indent=4))

    # Extract the message and sender
    for event in data['events']:
        message_text = event['message']['text']
        user_id = event['source']['userId']
        timestamp = event['timestamp']

        # Store message for later display
        messages.append({
            "text": message_text,
            "user": user_id,
            "timestamp": timestamp
        })

    return jsonify({"status": "success"})

# A simple page to display all the messages received
@app.route("/alerts", methods=["GET"])
def alerts():
    # Display the stored messages
    return jsonify(messages)

# Deploy the app to a test environment
if __name__ == "__main__":
    app.run(debug=True, port=5000)

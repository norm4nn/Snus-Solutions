from flask import Flask, render_template, request

app = Flask(__name__)

# Static list to store chat messages
chat_messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        sender = "User"
        chat_messages.append({"sender": sender, "message": message})
        response = generate_response(message)
        chat_messages.append({"sender": "Helper", "message": response})

    return render_template("index.html", chat_messages=chat_messages)

def generate_response(message):
    # This is a placeholder function to simulate a response from the server
    # Replace this with your actual logic to generate a response
    if "hello" in message.lower():
        return "Hello there! How can I assist you today?"
    else:
        return "I'm sorry, I didn't quite understand your request."

if __name__ == "__main__":
    app.run(debug=True)
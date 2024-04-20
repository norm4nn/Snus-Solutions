from flask import Flask, render_template, request
from openai import OpenAI
from Constansts import API_KEY

app = Flask(__name__)
client = OpenAI(api_key=API_KEY)

# Static list to store chat messages
chat_messages = []

is_waiting_for_response = False


@app.route("/", methods=["GET", "POST"])
def index():
    global is_waiting_for_response

    if request.method == "POST":
        if "message" in request.form:
            # Handle user message
            if not is_waiting_for_response:
                message = request.form.get("message")
                sender = "<b>User</b>"
                chat_messages.append({"sender": sender, "message": message})
                is_waiting_for_response = True  # Set the flag to True

                response = generate_response(message)

                chat_messages.append({"sender": "<b style='color:DarkGreen;'>Helper</b>", "message": response})
                is_waiting_for_response = False  # Reset the flag to False

        else:
            # Handle form submission
            gender = request.form.get("gender")
            occupation = request.form.get("occupation")
            age = request.form.get("age")
            family = request.form.get("family")
            working_years = request.form.get("working_years")
            products_bought = request.form.get("products_bought")

            # Process the form data as needed
            print(f'Gender: {gender}')
            print(f'Occupation: {occupation}')
            print(f'Age: {age}')
            print(f'Family: {family}')
            print(f'Working Years: {working_years}')
            print(f'Products Bought: {products_bought}')

            # You can add your logic here to handle the form data

    return render_template("index.html", chat_messages=chat_messages, is_waiting_for_response=is_waiting_for_response)


def generate_response(message):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a computer hardware store assinstant. Your task is to recommend "
                                          "products to clients. You can only recommend following products: Laptop "
                                          "gameing1, keybord ultra31, mouse gamer23. Reply only in pure text."},

            {"role": "user", "content": f"{message}"}
        ]
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=True)
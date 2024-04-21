from flask import Flask, render_template, request
from openai import OpenAI
from Constansts import API_KEY
import utils
import pandas as pd
from recommender import Customer, recommend_products
import torch
from model_class import SpendingsPredictor

app = Flask(__name__)
client = OpenAI(api_key=API_KEY)
SAVE_PATH = "spendings_predictor.pt"

# Static list to store chat messages
chat_messages = []

is_waiting_for_response = False
laptops = pd.read_csv("laptops_data.csv")
keyboards = pd.read_csv("keyboards_data.csv")
model = torch.load(SAVE_PATH)
user_info = {}
products = []


@app.route("/", methods=["GET", "POST"])
def index():
    global is_waiting_for_response, products, user_info
    # mapped_customer = utils.map_customer(["Male", 30, "Engineer", 7, 2, 3, "No", "No", "Cat_4"])
    #
    # # You can add your logic here to handle the form data
    # model_output = model(mapped_customer)
    # values = model_output.detach().numpy()
    # customer = Customer(values[0, 0], values[0, 2], "Engineer", values[0, 1])
    # products = recommend_products(customer, laptops, keyboards)
    #
    # products = [products[0].loc[:, ["Laptop", "Price", "Discounted"]],
    #             products[1].loc[:, ["Name", "Price", "Discounted"]]]

    if request.method == "POST":

        if "age" in request.form:
            user_info["gender"] = request.form.get("gender")
            user_info["occupation"] = request.form.get("occupation")
            user_info["age"] = request.form.get("age")
            user_info["family"] = request.form.get("family")
            user_info["working_years"] = request.form.get("working_years")
            user_info["products_bought"] = request.form.get("products_bought")
            print("user changed")

            products = generate_products()

            # mapped_customer = utils.map_customer([gender, int(age), occupation, int(working_years), int(family), int(products_bought), "No", "No", "Cat_4"])
            #
            # # You can add your logic here to handle the form data
            # model_output = model(mapped_customer)
            # values = model_output.detach().numpy()
            # customer = Customer(values[0, 0], values[0, 2], occupation, values[0, 1])
            # products = recommend_products(customer, laptops, keyboards)
            #
            # products = [products[0].loc[:, ["Laptop", "Price", "Discounted"]], products[1].loc[:, ["Name", "Price", "Discounted"]]]
            # print(products)

        if "message" in request.form:
            # Handle user message
            if not is_waiting_for_response:
                message = request.form.get("message")
                sender = "<b>User</b>"
                chat_messages.append({"sender": sender, "message": message})
                is_waiting_for_response = True  # Set the flag to True

                response = generate_response(message, products)
                print()

                chat_messages.append({"sender": "<b style='color:DarkGreen;'>Helper</b>", "message": response})
                is_waiting_for_response = False  # Reset the flag to False

    return render_template("index.html", chat_messages=chat_messages, is_waiting_for_response=is_waiting_for_response)


def generate_products():
    global user_info
    mapped_customer = utils.map_customer(
        [user_info["gender"], int(user_info["age"]), user_info["occupation"], int(user_info["working_years"]),
         int(user_info["family"]), int(user_info["products_bought"]), "No", "No", "Cat_4"])

    # You can add your logic here to handle the form data
    model_output = model(mapped_customer)
    values = model_output.detach().numpy()
    customer = Customer(values[0, 0], values[0, 2], user_info["occupation"], values[0, 1])
    products = recommend_products(customer, laptops, keyboards)

    products = [products[0].loc[:, ["Laptop", "Price", "Discounted"]],
                products[1].loc[:, ["Name", "Price", "Discounted"]]]

    print("products generated")
    print(products)
    return products


def generate_response(message, products):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a computer hardware store assinstant. Your task is to recommend "
                                          f"products to clients. You can only recommend following products: {products}"
                                          f"In your recommendation include price and offer discount based on provided "
                                          f"data. If discounted price is same as normal price don't mention it. "
                                          f"Dont recommend anything else. Reply only in pure text dont use ** **"},

            {"role": "user", "content": f"{message}"}
        ]
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=True)
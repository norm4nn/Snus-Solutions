from dataclasses import dataclass
import numpy as np
import pandas as pd



@dataclass
class Customer:
    def __init__(self, funds: int = None, possible_discount: float = None, profession: str = None, power: int = None):
        self.funds = funds
        self.possible_discount = possible_discount
        self.profession = profession
        self.power = power

def recommend_products(customer: Customer, *args) -> list[pd.DataFrame]:
    if not isinstance(customer, Customer):
        raise ValueError("Input must be a Customer object")

    def filter_products(products):
        st_dev = np.std(products["Normalized"]) * customer.power
        pred_products = products[products["Profession"].str.contains(customer.profession)]
        pred_products = pred_products[(pred_products["Normalized"] > customer.funds - st_dev) & (pred_products["Normalized"] < customer.funds + st_dev)]
        return pred_products
    
    def calculate_discount(products):
        prod_mean = np.mean(products["Price"])
        print(prod_mean)
        products["Discounted"] = products["Price"]-prod_mean
        for index, discounted_price in products["Discounted"].items():
            # Calculate discounted price for the current product
            new_discounted_price = products.at[index, "Price"] - max(discounted_price, 0) * customer.possible_discount
            # Update the value in the DataFrame
            products.at[index, "Discounted"] = new_discounted_price
        products["Discounted"] = products["Discounted"].apply(lambda x: round(x, 2))
        return products


    """pred_laptops = filter_products(laptops)
    pred_keyboards = filter_products(keyboards)"""

    predictions = [filter_products(arg) for arg in args]
    predictions = [calculate_discount(p) for p  in predictions]

    return predictions
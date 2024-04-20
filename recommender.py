from dataclasses import dataclass
import pandas as pd
import numpy as np

@dataclass
class Customer:
    def __init__(self, funds: int = None, possible_discount: float = None, profession: str = None, power: int = None):
        self.funds = funds
        self.possible_discount = possible_discount
        self.profession = profession
        self.power = power

laptops = pd.read_csv("laptops_data.csv")
keyboards = pd.read_csv("keyboards_data.csv")

def recommend(customer: Customer):
    return predictor(customer, laptops, "Final Price"), predictor(customer, keyboards, "Price")

def predictor(customer: Customer, df: pd.DataFrame, column: str):
    pred_key = df[df["Profession"] == customer.profession]
    pred_key = pred_key.sort_values(by=column)
    mean = pred_key[column].mean()

    quantile = 0.5
    match customer.power:
        case 1:
            quantile = 1/3
            quant = np.quantile(pred_key[column], quantile)
            pred_key = pred_key[pred_key[column] < mean-quant]
        case 2:
            quantile = 1/3
            quant = np.quantile(pred_key[column], quantile)
            pred_key = pred_key[pred_key[column] > mean-quant]
            quantile = 2/3
            quant = np.quantile(pred_key[column], quantile)
            pred_key = pred_key[pred_key[column] < mean+quant]
        case 3: 
            quantile = 2/3
            quant = np.quantile(pred_key[column], quantile)
            pred_key = pred_key[pred_key[column] > mean+quant]
    return pred_key
import utils
import pandas as pd
from recommender import Customer, recommend_products
import torch
from model_class import SpendingsPredictor

SAVE_PATH = "spendings_predictor.pt"
model = torch.load(SAVE_PATH)

gender = ["Male", "Female"]
age = [i for i in range(20, 80)]

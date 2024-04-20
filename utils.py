from typing import List
from sklearn.preprocessing import MinMaxScaler
import torch
from sklearn.preprocessing import LabelEncoder

import numpy as np
import pandas as pd

data = pd.read_csv("customers.csv")

mapping_string_to_int = {}

label_encoder = LabelEncoder()
string_fields = ['Gender_x', 'Profession', 'Spending_Score']
for string_field in string_fields:
    old = data[string_field].copy()
    data[string_field] = label_encoder.fit_transform(data[string_field])
    new = data[string_field]
    pairs = zip(old, new)


    for key, val in pairs:
        mapping_string_to_int[key] = val


scaler = MinMaxScaler()
mins_and_ranges = []

for field_name in data.columns:
    data[field_name] = scaler.fit_transform(data[[field_name]])
    mins_and_ranges.append((scaler.data_min_, scaler.data_range_))


def map_customer(customer: List):
    strings_fields_idx = [0, 2]
    for i in strings_fields_idx:
        customer[i] = mapping_string_to_int[customer[i]]

    for i in range(len(customer)):
        customer[i] -= mins_and_ranges[i][0]
        customer[i] /= mins_and_ranges[i][1]

    customer = torch.tensor(customer).to(torch.float32)
    return customer.reshape((1, 7))
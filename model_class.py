import torch
from torch import nn
from torch import sigmoid


class SpendingsPredictor(nn.Module):
    def __init__(self, input_size: int, dropout_p: float = 0.5):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ReLU(),
            nn.Dropout(dropout_p),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(dropout_p),
            nn.Linear(128, 3)
        )

    def forward(self, x):
        return self.mlp(x)

    def predict_proba(self, x):
        return sigmoid(self(x))

    def predict(self, x):
        y_pred_score = self.predict_proba(x)
        return torch.argmax(y_pred_score, dim=1)

# # NN 3
class SpendingsPredictor3(nn.Module):
    def __init__(self, input_size: int, dropout_p: float = 0.5):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.Sigmoid(),
            nn.Dropout(dropout_p),
            nn.Linear(256, 128),
            nn.Sigmoid(),
            nn.Dropout(dropout_p),
            nn.Linear(128, 3)
        )

    def forward(self, x):
        return self.mlp(x)

    def predict_proba(self, x):
        return sigmoid(self(x))

    def predict(self, x):
        y_pred_score = self.predict_proba(x)
        return torch.argmax(y_pred_score, dim=1)
    
    
# # NN 4
class SpendingsPredictor4(nn.Module):
    def __init__(self, input_size: int, dropout_p: float = 0.5):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.PReLU(),
            nn.Dropout(dropout_p),
            nn.Linear(256, 128),
            nn.PReLU(),
            nn.Dropout(dropout_p),
            nn.Linear(128, 3)
        )

    def forward(self, x):
        return self.mlp(x)

    def predict_proba(self, x):
        return sigmoid(self(x))

    def predict(self, x):
        y_pred_score = self.predict_proba(x)
        return torch.argmax(y_pred_score, dim=1)
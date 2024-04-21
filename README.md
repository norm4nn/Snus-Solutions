# HardwareHelper

Welcome to the HardwareHelper! This Flask web application utilizes machine learning and OpenAI's language model to provide personalized product recommendations based on user input.

## Features

- **Personalized Recommendations**: Users can receive tailored product recommendations based on their demographic information and preferences.
- **Real-time Interaction**: The system engages in real-time conversation with users, gathering necessary data and providing recommendations instantly.
- **Product Selection**: Recommendations include both laptops and keyboards, offering users a comprehensive selection to choose from.
- **Discounted Offers**: Users are informed about discounted prices, enhancing the value proposition of recommended products.

## Getting Started

To run the application locally, follow these steps:

```bash
git clone https://github.com/norm4nn/Snus-Solutions.git
cd Snus-Solutions
pip install -r requirements.txt
```

Obtain an API key from OpenAI and create `Constansts.py` with your API key as API_KEY variable.

Ensure you have the necessary data files (`laptops_data.csv` and `keyboards_data.csv`) in the project directory.

```bash
python wsgi.py
```

Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Upon accessing the application, fill out the provided form with your demographic information and preferences.
2. Once submitted, the system generates personalized product recommendations based on your input.
3. Engage in a conversation with the system by typing your messages in the chat interface.
4. Receive product recommendations and relevant information about discounts in real-time.
5. Enjoy a seamless and personalized shopping experience!

## Dependencies

- Flask: Web application framework for Python.
- OpenAI: Python client for the OpenAI API.
- Pandas: Data manipulation and analysis library.
- Torch: PyTorch deep learning framework.

## User Interface

![image](https://github.com/norm4nn/Snus-Solutions/assets/50834734/1f814b5a-8719-4db5-a1a2-2864cfa3ecea)


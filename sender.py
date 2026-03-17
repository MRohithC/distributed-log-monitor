import requests
import random

sample_logs = [
    {"service": "auth-service", "level": "INFO", "message": "User logged in"},
    {"service": "auth-service", "level": "ERROR", "message": "Invalid password"},
    {"service": "payment-service", "level": "INFO", "message": "Payment successful"},
    {"service": "payment-service", "level": "ERROR", "message": "Card declined"},
    {"service": "order-service", "level": "WARNING", "message": "Order delayed"}
]

for log in sample_logs:
    response = requests.post("http://127.0.0.1:5000/logs", json=log)
    print(response.status_code, response.json())
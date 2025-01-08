import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Функція для отримання курсу валют на певну дату
def get_exchange_rate(date: str, currency_code: str = 'USD'):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&date={date}&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['rate']
        else:
            return None
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

# Отримання курсу за попередній тиждень
currency_code = 'USD'  # Можна змінити на інший код валюти, наприклад, EUR, GBP тощо
end_date = datetime.now() - timedelta(days=1)  # Вчорашня дата
start_date = end_date - timedelta(days=6)  # Тиждень тому

dates = []
rates = []

for i in range(7):
    date = (start_date + timedelta(days=i)).strftime('%Y%m%d')
    try:
        rate = get_exchange_rate(date, currency_code)
        if rate:
            dates.append((start_date + timedelta(days=i)).strftime('%Y-%m-%d'))
            rates.append(rate)
    except Exception as e:
        print(f"Дата: {date}, Помилка: {e}")

# Побудова графіку
plt.figure(figsize=(10, 5))
plt.plot(dates, rates, marker='o', linestyle='-', color='b')
plt.title(f"Зміна курсу {currency_code} за останній тиждень")
plt.xlabel("Дата")
plt.ylabel("Курс")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

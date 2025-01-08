import requests
from datetime import datetime, timedelta

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

print(f"Курс {currency_code} за попередній тиждень:\n")

for i in range(7):
    date = (start_date + timedelta(days=i)).strftime('%Y%m%d')
    try:
        rate = get_exchange_rate(date, currency_code)
        if rate:
            print(f"Дата: {date}, Курс: {rate:.2f}")
        else:
            print(f"Дата: {date}, Курс недоступний")
    except Exception as e:
        print(f"Дата: {date}, Помилка: {e}")

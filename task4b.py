from telethon import TelegramClient

api_id = '24177136'
api_hash = 'af0855d1b382e7c84b21371fb59de65e'

# Створення клієнта
client = TelegramClient('session_name', api_id, api_hash)

# Функція для відправки повідомлення
async def send_message(recipient, message):
    try:
        # Відправка повідомлення
        await client.send_message(recipient, message)
        print(f"Повідомлення успішно надіслано: {message} -> {recipient}")
    except Exception as e:
        print(f"Помилка під час відправки повідомлення: {e}")

# Основна функція
async def main():
    try:
        # Авторизація
        print("Підключення до Telegram...")
        await client.start()
        print("Успішно авторизовано!")

        # Введення отримувача та тексту повідомлення
        recipient = input("Введіть username, ID або номер телефону отримувача (наприклад, @example_user): ")
        message = input("Введіть текст повідомлення: ")

        # Відправка повідомлення
        await send_message(recipient, message)

    except Exception as e:
        print(f"Помилка: {e}")

# Запуск основного блоку
with client:
    client.loop.run_until_complete(main())

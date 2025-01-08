#Перед запуском коду преконайтеся, що 2FA вимкнена!!!

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

api_id = '24177136'
api_hash = 'af0855d1b382e7c84b21371fb59de65e'

# Створення клієнта
client = TelegramClient('session_name', api_id, api_hash)


# Функція для отримання списку користувачів чату/групи з лімітом
async def get_chat_members(chat_username, limit=100):
    try:
        # Отримання інформації про чат
        chat = await client.get_entity(chat_username)
        print(f"Назва чату: {chat.title}")

        # Отримання списку учасників
        participants = await client.get_participants(chat, limit=limit)
        print(f"Учасники чату (перших {limit} учасників):")
        for user in participants:
            print(f"ID: {user.id}, Ім'я: {user.first_name}, Прізвище: {user.last_name}, Username: {user.username}")
    except Exception as e:
        print(f"Помилка: {e}")


# Основна функція
async def main():
    try:
        # Авторизація
        print("Підключення до Telegram...")
        await client.start()
        print("Успішно авторизовано!")

        # Отримання інформації про користувача
        me = await client.get_me()
        print(f"Ви увійшли як: {me.first_name} (@{me.username})")

        # Введення username або ID чату/групи
        chat_username = input("Введіть username або ID чату/групи (наприклад, @example_chat): ")
        await get_chat_members(chat_username, limit=100)

    except SessionPasswordNeededError:
        # Якщо потрібен пароль 2FA
        password = input("Введіть ваш пароль двофакторної аутентифікації: ")
        await client.sign_in(password=password)
        print("Успішно авторизовано з використанням 2FA!")
        # Повторне виконання після авторизації
        chat_username = input("Введіть username або ID чату/групи (наприклад, @example_chat): ")
        await get_chat_members(chat_username, limit=100)

    except Exception as e:
        print(f"Помилка: {e}")


# Запуск основного блоку
with client:
    client.loop.run_until_complete(main())
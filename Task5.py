import telebot
from telebot import types

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from @BotFather
BOT_TOKEN = '7733459950:AAGBU_0aSODJ-11nzHxAkUPqKwjcbr45GdY'
bot = telebot.TeleBot(BOT_TOKEN)

# Command handlers
@bot.message_handler(commands=['start', 'menu'])
def send_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    whisper_btn = types.KeyboardButton('Whisper')
    scream_btn = types.KeyboardButton('Scream')
    markup.add(whisper_btn, scream_btn)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

# State tracking dictionary
user_states = {}

@bot.message_handler(func=lambda message: message.text == 'Whisper')
def whisper_handler(message):
    user_states[message.chat.id] = 'whisper'
    bot.send_message(message.chat.id, "Please send a message to whisper.")

@bot.message_handler(func=lambda message: message.text == 'Scream')
def scream_handler(message):
    user_states[message.chat.id] = 'scream'
    bot.send_message(message.chat.id, "Please send a message to scream.")

@bot.message_handler(func=lambda message: True)
def echo_handler(message):
    user_state = user_states.get(message.chat.id)
    if user_state == 'whisper':
        bot.send_message(message.chat.id, message.text.lower())
        user_states.pop(message.chat.id, None)  # Reset state after processing
    elif user_state == 'scream':
        bot.send_message(message.chat.id, message.text.upper())
        user_states.pop(message.chat.id, None)  # Reset state after processing
    else:
        bot.send_message(message.chat.id, "I didn't understand that. Use /menu to see options.")

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(none_stop=True)

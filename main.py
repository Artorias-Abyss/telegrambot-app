import telebot
import webbrowser

bot = telebot.TeleBot('7843121335:AAFsLS-YUMnxg9clLWZl4oxe-jYSGNHvmyo')

@bot.message_handler(commands=['site', 'website'])
def main (message):
    webbrowser.open('https://ru.pinterest.com')

@bot.message_handler(commands=['start', 'hello'])
def main (massage):
    bot.send_message(massage.chat.id, 'I am Malenia. Blade of Miquella. And I have never known defeat.')

@bot.message_handler(commands=['help'])
def main (massage):
    bot.send_message(massage.chat.id, 'Helping menu.')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет' :
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(non_stop=True)

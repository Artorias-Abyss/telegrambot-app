import telebot
from telebot import types

bot = telebot.TeleBot('7843121335:AAFsLS-YUMnxg9clLWZl4oxe-jYSGNHvmyo')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(
        text = 'Взглянем на сайт ?'
    )
    markup.add(btn1)
    btn2 = types.KeyboardButton(
        text='Delete steps'
    )
    btn3 = types.KeyboardButton(
        text='Edit'
    )
    markup.row(btn2, btn3)
    file = open('./img/photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, 'Привет родной', reply_markup=markup)

    bot.register_next_step_handler(message, on_click)

def on_click (message):
    if message.text == 'Взглянем на сайт ?':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Delete object':
        bot.send_message(message.chat.id, 'All right')

@bot.message_handler(content_types=['photo', 'document'])
def get_foto(message):
    markup = types.InlineKeyboardMarkup()
    butten = types.InlineKeyboardButton(
        text = 'Move on the OG-Music',
        url = 'https://www.youtube.com/watch?v=LBbANuA6oaw&list=PLGLc7MdEGNSb41F8m8siYJsCysp7u3Ktp&index=32'
    )
    markup.add(butten)
    deleter = types.InlineKeyboardButton(
        text='Deleat steps',
        callback_data='delete'
    )
    editer = types.InlineKeyboardButton(
        text='Edit',
        callback_data='edit'  # исправлено с 'Edit' на 'edit' (регистр должен совпадать)
    )
    markup.row(deleter, editer)
    bot.reply_to(message, 'How cool !', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text(
            'Edit text',
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id
        )

bot.polling(non_stop=True)
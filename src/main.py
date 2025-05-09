import telebot
import os
from anamnese import handle_anamnese

# Получение токена из переменной окружения
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Здравствуйте! Я GPT-помощник по радиационной онкологии.\n"
        "Напишите /anamnese для начала сбора анамнеза."
    )

@bot.message_handler(commands=["anamnese"])
def start_anamnese(message):
    bot.reply_to(message, "Начинаем сбор анамнеза.")
    handle_anamnese(bot, message)

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)



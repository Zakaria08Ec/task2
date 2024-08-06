import telebot
from googletrans import Translator, LANGUAGES

API_TOKEN = '7381647865:AAGgOqOvOArh0ANr7Xj8VqxqsSbUGHt379w'

translator = Translator()
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Use the command /translate <language> <text> to translate your message.\n"
                          "For example: /translate en Hello")

@bot.message_handler(commands=['translate'])
def translate(message):
    try:
        parts = message.text.split(maxsplit=2)
        if len(parts) < 3:
            bot.reply_to(message, "Usage: /translate <language> <text>")
            return

        target_lang = parts[1]
        text_to_translate = parts[2]

        if target_lang not in LANGUAGES:
            bot.reply_to(message, f"Invalid language. Use one of the following: {', '.join(LANGUAGES.keys())}")
            return

        translated = translator.translate(text_to_translate, dest=target_lang)
        bot.reply_to(message, f"Translation in {LANGUAGES[target_lang]}: {translated.text}")

    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

bot.polling()

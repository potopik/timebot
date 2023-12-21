import telebot
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello!')

@bot.message_handler(content_types=['text'])
def echo_message(message):
    text = f'Символов в сообщении: {len(message.text)}'
    bot.reply_to(message, text)

if __name__ == "__main__":
    print('bot is runnung')
    bot.polling()
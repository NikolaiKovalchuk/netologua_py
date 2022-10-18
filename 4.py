import telebot

token = '570'

bot = telebot.TeleBot(token)
word = "Nikola"

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)

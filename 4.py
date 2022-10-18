import telebot

token = '570'

bot = telebot.TeleBot(token)
word = "Nikola"

@bot.message_handler(content_types=["text"])
def echo(message):
    if word in message.text:
        text = 'Ба! Знакомые все лица'
    else:
        text = message.text
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

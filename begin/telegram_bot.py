#pip install pytelegrambotapi
# telegram -> BotFather - батя всех ботов
# newbot и даем ему имя
# делаем простого эхо бота
import telebot

TOKEN = 'TOKEN'

bot = telebot.TeleBot(TOKEN)

#@bot.message_handler(commands=['start', 'help'])
#def command_help(message):
#    bot.reply_to(message, "Hello, did someone call for help?")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    #bot.reply_to(message, message.text)  #  пересылает сообщение
    bot.send_message(message.chat.id, message.text) #вот тепеерь он будет отвечать :))

bot.polling( none_stop = True)

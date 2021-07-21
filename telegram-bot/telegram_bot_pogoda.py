# Бот будет показывать погоду
import pyowm
from pyowm import OWM # для погоды
from pyowm.commons.enums import SubscriptionTypeEnum # для погоды
import telebot # для бота

# Иницилизация бота телеграм
TOKEN = 'TOKEN' # токен телеграм бота
bot = telebot.TeleBot(TOKEN)

# иницилизация погоды
config = {
    'subscription_type': SubscriptionTypeEnum.FREE,
    'language': 'ru',
    'connection': {
        'use_ssl': True,
        'verify_ssl_certs': True,
        'use_proxy': False,
        'timeout_secs': 5
    },
    'proxies': {
        'http': 'http://user:pass@host:port',
        'https': 'socks5://user:pass@host:port'
    }
}
owm = OWM('TOKEN', config=config)
######################

@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temper = w.temperature('celsius')['temp']

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Тепература сейчас в районе " + str(temper)  + "\n\n"

    if temper < 10:
        answer += "Одевайся теплее, на улице холодрыга"
    elif temper < 20:
        answer += "Cейчас на улице холодно, одевайся теплее. "
    else:
        answer += "На улице тепло, можно идти в трусах :)"

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True)






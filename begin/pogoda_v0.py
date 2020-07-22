#Будем показывать погоду пользователю.
# pip install  pyowm
import pyowm
from pyowm import OWM
from pyowm.commons.enums import SubscriptionTypeEnum

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

place = input("Где интересует погода? Вводим: ")



mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

w.wind()
w.humidity
w.temperature('celsius')
observation_list = mgr.weather_around_coords(-22.57, -43.12)
temper = w.temperature('celsius')['temp']
wind = w.wind()

#print(w)
#print(w.temperature('celsius'))
#print(w.wind())

print(f"В городе {place} сейчас {w.detailed_status}, температура {temper} ")

if temper < 10:
    print("Одевайся теплее, на улице холодрыга")
elif temper < 20:
    print("Cейчас на улице холодно, одевайся теплее. ")
else:
    print(" На улице тепло, можно идти в трусах :)")
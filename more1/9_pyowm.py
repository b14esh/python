# https://pypi.org/project/pyowm/
# https://github.com/csparpa/pyowm
# https://pyowm.readthedocs.io/en/latest/
# https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html
# pip install pyowm
# https://openweathermap.org/
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


owm = OWM('TOKEN', config=config)  # You MUST provide a valid API key
mgr = owm.weather_manager()
city = "Санкт-Петербург"
#city = input("Введите город: ")

observation = mgr.weather_at_place('city')
w = observation.weather
t = w.temperature('celsius')

print(w)

print(f" В Санкт-Петербурге : \n\tТемпература {w.temperature('celsius')['temp']} по Целсию. \n\tСкорость ветра {w.wind()['speed']} м/c. \n\tНа улице \"{w.detailed_status}\".")
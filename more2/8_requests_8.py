## Timeout
## Сессиии
## Количество попыток

#with requests.Session() as session:
#    session.auth = ('Username', getpass())
#    response = session.get("https://api.github.com/user")
    ### do a Lot staff
#print(response.json())

# Количество попыток
import requests
from requests.exceptions import Timeout
from getpass import getpass
from requests.adapters import  HTTPAdapter

adapter = HTTPAdapter(max_retries=3) # вот тут кол-во попыток

with requests.Session() as session:
    session.mount('https://api.github.com', adapter)
    session.auth = ("Username", getpass())

    try:
        session.get("https://api.github.com/user")
    except ConnectionError as err:
        print(f"Failed to connect: {err}")
    else:
        print('OK')

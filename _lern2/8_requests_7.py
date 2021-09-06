#  ## По умолчанию request  не устанавливает никаких тайммаутов
## Timeout

import requests
from requests.exceptions import Timeout
from getpass import getpass
try:
    response = requests.get("https://b14esh.com", timeout = 1)
except Timeout:
    print("The request time out")

print(response)



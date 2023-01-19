import webbrowser
import json
from urllib.request import urlopen

print("Время найти сайт.")
site = input("Ввыдите сайт: ")
era = input("Введите дату, пример 20150720: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
   old_site = data["archived_snapshots"]["closest"]["url"]
   print("Нашли копию: ", old_site)
   print("Теперь он должен появиться в вашем браузере.")
   webbrowser.open(old_site)
except:
    print("Извините, не удалось найти", site)

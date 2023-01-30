import webbrowser
import requests

print("Время найти сайт в webarhiv.")
site = input("Ввыдите сайт: ")
era = input("Введите дату, пример 20150720: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
try:
   old_site = data["archived_snapshots"]["closest"]["url"]
   print("Нашли копию: ", old_site)
   print("Теперь он должен появиться в вашем браузере.")
   webbrowser.open(old_site)
except:
    print("Извините, не удалось найти", site)

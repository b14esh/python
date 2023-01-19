import os
if os.path.exists("oldname.txt"):
  print("Файл oldname.txt существует и будет переименован в newname.txt ")
  os.rename('oldname.txt','newname.txt')
if os.path.exists("newname.txt"):
  print("Фай newname.txt существует и будет переименован в oldname.txt")  
  os.rename('newname.txt', 'oldname.txt')
else:
  print("Файлов oldanme.txt и newname.txt не обнаруженно! \nДелать нечего! \nЗавершаем работу.")
import os


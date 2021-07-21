# Модуль datetime
from datetime import datetime
from datetime import date
from  datetime import time
from datetime import timedelta

d1 = date(2020,8,24)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)

t1 = time(22, 10, 44)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)


print(date.today())


print(date.max)
print(date.min)

print(time.min)
print(time.max)

dt = datetime(2020, 4, 12, 19, 00)
print(dt)

print(dt.date().year)
print(dt.time().hour)

print(datetime.min)
print(datetime.max)

now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.hour)
print(now.minute)
print(now.second)

new_dt = now.replace(year=2015) # подемена на примере года
print(new_dt)


# Парсинг времени
dt = datetime.strptime("30/07/2020", "%d/%m/%Y")
print(dt)
dt = datetime.strptime("30/07/2020 10:10", "%d/%m/%Y %H:%M")
print(dt)
dt = datetime.strptime("07-30-2020 15:20", "%m-%d-%Y %H:%M")
print(dt)
dt = datetime.strptime("2020-07-30", "%Y-%m-%d")
print(dt)

# Передача времени
import locale
locale.setlocale(locale.LC_ALL, "") # Установка локали
print(locale.setlocale(locale.LC_ALL, "")) # Показать что му там установили

now = datetime.now()
print(now.strftime('%Y-%m-%d (%a)'))
print(now.strftime('%Y-%B-%d число (%A)'))

# Дельта времени
delta1 = timedelta(days=3, hours=2, minutes=10)
print(delta1)
delta2 = timedelta(days=2, hours=1, minutes=4)
print(delta1-delta2)
print(delta2-delta1)

my_birthdate = date(1986, 4, 13)
delta = date.today() - my_birthdate
print(type(delta))

my_age = int(delta.days/365)
print(my_age)


ba_birthday = date(1987, 4, 21)
am_i_older = my_birthdate < ba_birthday
print(am_i_older)

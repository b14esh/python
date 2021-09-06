# Статические методы

class StaticTest:
    x = 1

t1 = StaticTest()

print(f'Vis instance:{t1.x}')
print(f'via class:{StaticTest.x}')

t1.x = 2

print(f'Vis instance:{t1.x}')
print(f'via class:{StaticTest.x}')

StaticTest.x = 3

print(f'Vis instance:{t1.x}')
print(f'via class:{StaticTest.x}')


# далее
# Python позволяет в классе иметь только один конструктор

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f"{self.month} - {self.day} - {self.year}"

    @classmethod
    def millenium_c(cls, month, day):
        return cls(month, day, 2000)

    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)

d1 = Date.millenium_c(6, 9)
d2 = Date.millenium_s(6,9)

print(d1.display())
print(d2.display())

class DateTime(Date):
    def display(self):
        return f"{self.month} - {self.day} - {self.year} - 00:00:00PM"

dt1 = DateTime(10, 10, 1990)
dt2 = DateTime.millenium_s(10,10)
#dt2 = DateTime.millenium_c(10,10)

print(isinstance(dt1, DateTime))
print(isinstance(dt2, DateTime))

print(dt1.display())
print(dt2.display())


### Пример использования статического декоратора
class StrConverter:
    @staticmethod
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        return value

    @staticmethod
    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        return value

print(StrConverter.to_str('\x41'))
print(StrConverter.to_str('A'))

print(StrConverter.to_bytes('\x41'))
print(StrConverter.to_bytes('A'))
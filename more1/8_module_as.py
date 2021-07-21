# подключить функцию под другим именем
# пригодится например если вдруг у вас уже есть своя функция
# пример на модуле math функция sqrt
# Лутче этого не допускать
from math import sqrt as my_sqrt
def sqrt():
    print("my function")
print(my_sqrt(25))
sqrt()
# обычные словари
# до python 3.7 словари распечатовались игнорировали последовательность добавления
# обычному словарю не важна последовательность
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'
d2['c'] = 'C'

d3 = {}
d3['a'] = 'A'
d3['b'] = 'B'
d3['c'] = 'C'

for k, v in d1.items():
    print(k, v)

for k, v in d2.items():
    print(k,v)
for k, v in d3.items():
    print(k, v)

print(d1==d2) #True
print(d1==d3) #True

# по итогу d1 = d2 = d3

print("\n")

# Загружаем библиотеку OrderedDict
from collections import OrderedDict
# OrderedDict учитывает порядок ключ: значение
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'
d2['c'] = 'C'

d3 = OrderedDict()
d3['a'] = 'A'
d3['b'] = 'B'
d3['c'] = 'C'

print(d1==d2) #False
print(d1==d3) #True

# По итогу d1 = d2 и d1 != d3
s = 'Все лето мы пили пиво. Вот как-то открываю дверь, а на пороге Чебурашка, весь такой пьяный-пьяный, и бутылка из кармана торчит.'
slova = {'пили':'читали', 'пиво':'книги', 'пьяный':'начитанный', 'бутылка':'энциклопедия'}
# Словари во многом похожи на списки, но значения в них записаны парами: 
# ключ и значение. По ключу можно узнать значение. 
# Можно считать, что в списках ключи — это индексы (0, 1, 2...), а в словарях — строки.
print(f"А было в тексте вот это вот: \n {s}")

for key in slova:
    s = s.replace(key, slova[key])
print(f"А стало вот это: \n {s}")


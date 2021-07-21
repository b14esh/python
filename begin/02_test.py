from mod16 import pp
favorite_songs = {
'Тополиный пух': 'Иванушки international',
'Город золотой': 'Аквариум',
'Звезда по имени Солнце': 'Кино',
'Группа крови': 'Кино'
}
for track in favorite_songs:
     print(track + ' это песня группы ' + favorite_songs[track])
pp()
for music_band in favorite_songs.values():
     print('Доктор, я больше не могу слушать группу ' + music_band)
pp()
for track, music_band in favorite_songs.items():
     print(track + ' это песня группы ' + music_band)
pp()
songs1 = {
'Три белых коня',
'Happy new year',
'Снежинка'
}
songs2 = {
'Last christmas',
'Снежинка',
'Happy new year'
}
print(songs1.union(songs2))
(pp)

english = {
'рука': 'hand',
'нога': 'leg',
'разработчик': 'developer'
}
# доступ по ключу: как по-английски рука?
print(english['рука'])
english['рука'] = 'arm'
# значение для ключа 'рука'
# поменялось с 'hand' на 'arm'
pp()

friends = {
    'Роби Тобинсон': ['Металлий Вутко', 'Лео Месси', 'Бен Франклин', 'Твентин Карантино'],
    'Металлий Вутко': ['Металлий Вутко'],
    'Лео Месси': ['Металлий Вутко'],
    'Бен Франклин': ['Металлий Вутко', 'Лео Месси', 'Твентин Карантино', 'Elina Shake', 'Айви Яптанго'],
    'Твентин Карантино': ['Бен Франклин'],
    'Elina Shake': ['Металлий Вутко', 'Лео Месси', 'Бен Франклин'],
    'Айви Яптанго': ['Бен Франклин', 'Твентин Карантино', 'Elina Shake']
}
#user = 'Роби Тобинсон'
#print(friends[user])
def get_friends(request, user):
    user_friends = friends[str(user)] # список друзей пользователя user
    friends_count = len(user_friends) # длина этого списка
    if friends_count == 1:
        return HttpResponse(f'У пользователя {user} один друг: {user_friends[0]}.')
    elif friends_count >=2 and friends_count <=4: # если количество друзей от 2 до 4 включительно, то
        friends_string = ', '.join(user_friends)
        return HttpResponse(f'У пользователя {user} {friends_count} друга: {friends_string}.')
    elif friends_count >4  :  # если количество друзей более 4, то
        friends_string = ', '.join(user_friends)
        return HttpResponse(f'У пользователя {user} {friends_count} друзей: {friends_string}.')
    else:
        return HttpResponse(f'У пользователя {user} нет друзей :(')

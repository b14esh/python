import json
filename = "user_setting.txt" # имя файла в который сохраняем
myfile = open(filename, mode='w', encoding="utf-8") # открываем файл для записи
player1 = {
    'PlayerName': "Chuvak",
    'Score': 345,
    'Awards': ["OR", "New", "ZZ"],
}

player2 = {
    'PlayerName': "Osip",
    'Score': 345,
    'Awards': ["WI", "TX", "Miss"],
}

mayplayer = [] # создали пустой массив
mayplayer.append(player1) # добавляем в массив словарь player1
mayplayer.append(player2) # добавляем в массив словарь player2

# ---------------- SAVE by JSON ---------------------
json.dump(mayplayer, myfile)
myfile.close()

# ----------------- LOAD
myfile = open(filename, mode='r', encoding='utf-8')
json_data = json.load(myfile)
for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Award is: " + str(user['Awards'][0]))
    print("Player Award is: " + str(user['Awards'][1]))
    print("Player Award is: " + str(user['Awards'][2]))
    print("--------------------------------------")
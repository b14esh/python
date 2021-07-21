contacts = {
    "Лось": "1234567",
    "Лис":"5555555",
    "Зубра":"999"

}

testing = input("Кого ищем?: ")
if testing in contacts:
    print(f"С именем \"{testing}\" есть в базе, \n его телефон   \"{contacts[testing]}\"")
else:
    print("ничего не нашлось")
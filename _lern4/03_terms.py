beer = input("Введите Yes, если пиво есть, и No, если его нет: ")
if beer.lower() == "yes" :
         x = input("Ну и сколько там его у тебя?: ")
         result = "С таким кол-вом " + str(x) + " ты долеко пойдешь"
else: 
   result = "И на что ты расчитываешь? Иди за пивом!"
print(f"{result}")
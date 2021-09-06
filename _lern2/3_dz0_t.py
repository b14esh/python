# что нашкодил учитель
import random
tries = 0
number = random.randint(1, 50)
print(number)
print("Привет я тут загодал число...")
while tries < 6:
    guess = int(input("Введите число от 1 до 50: "))
    tries+=1
    if guess < number:
        print("Твое число меньшне чем загаданное")
    if guess > number:
        print("Твое число больше чем загаданное")
    if guess == number:
        print(f"Поздравляю вы отгодали число, за {tries} попыток")
        break
    if tries != number and tries == 6:
        print(f"К сожелению вы не смогли отгодать за 6 попыток. Число было {tries}")
        break

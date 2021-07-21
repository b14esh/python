# игра в палочки
# нашкодил учитель

number_of_sticks = 10
player_turn = 1

while number_of_sticks > 0:
    print(f'How many stiks you take? {number_of_sticks}')
    taken = int(input())

    if taken < 1 or taken > 3:
        print(f"You tried to take {taken}. Allowed 1,2,3 stiks")
        continue

    number_of_sticks -= taken
    print(f"Stiks taken:{taken}\n")

    if number_of_sticks <= 0:
        print(f"No more stiks in game. \n Player {player_turn} has lost")

    player_turn == 1 if player_turn == 2 else 2
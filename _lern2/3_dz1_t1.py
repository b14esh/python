number_of_sticks = 10
player_turn = 1

def can_take(sticks):
    return sticks >= 1 and <= 3

def switch_player_turn(turn):
    return 1 if player_turn == 2 else 2

def end_of_game(sticks):
    return number_of_sticks <= 0

while (not end_of_game(number_of_sticks)):
    print(f'How many stiks you take? {number_of_sticks}')
    taken = int(input())

    if not can_take(taken):
        print(f"You tried to take {taken}. Allowed 1,2,3 stiks")
        continue

    number_of_sticks -= taken
    print(f"Stiks taken:{taken}\n")

    if end_of_game(number_of_sticks):
        print(f"No more stiks in game. \n Player {player_turn} has lost")
        break

    player_turn == switch_player_turn(player_turn)
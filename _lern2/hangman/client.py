from python.more2.hangman.game import Game
from python.more2.hangman.game_status import GameStatus


def chars_list_to_str(chars):
    return ''.join(chars)


game = Game()
word = game.generate_world()

letters_count = len(word)

print(f"The word consists of {letters_count} letters")
print("try to guess the world letters by letter")

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input("Pick a letter.\n")
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))

    print(f"Ramaining tries = {game.remaining_tries}")
    print(f"Tried letters: {chars_list_to_str(game.tried_letters)}")

if game.game_status == GameStatus.LOST:
    print("You're hunged! ")
    print(f"The word was: {game.word}")

else:
    print("Congratulations! You WON!")

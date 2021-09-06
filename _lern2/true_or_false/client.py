from python.more2.true_or_false.game import Game
from python.more2.true_or_false.game_result import GameResult
from python.more2.true_or_false.game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f"Questions asked:{result.questions_passed}. Mistakes made:{result.mistakes_made}")
    print(f"you won" if result.won else "You lost!")

#game = Game(file_path="data\\Questions.csv",  allowed_mistakes=3, end_of_game_handler=end_of_game_handler)
game = Game("data\\Questions.csv",  3, end_of_game_handler)

while game.game_status == GameStatus.IN_PROGRESS:
    # if game.is_last_question():
    #    print("No more questions.")
    #    break

    q = game.get_next_question()
    print("Do you believe in the next statement or questions? Enter 'y' and 'n' ")

    print(q.text)

    answer = input() == "y"

    if q.is_true == answer:
        print("Good job! You're right!")

    else:
        print("Oops, actually you're mistaken. Here is the explanation:" )
        print(q.explanation)

    game.give_answer(answer)

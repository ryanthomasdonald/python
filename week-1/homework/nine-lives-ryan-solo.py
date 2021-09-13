import random

words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]

secret_word = random.choice(words)
secret_word_list = list(secret_word)
heart_symbol = u"\u2764" + " "
guessed_word_correctly = False

print("Guess the secret word. You have nine tries.")

life = 9

while life >= 0:
    hearts = heart_symbol * life
    answer = input("Guess a letter: ")
    if answer.lower() == "a": #right answer
        print("Correct!")
        print("Game Board")
        print("[ " + hearts + "]")
    elif answer.lower() == "b": #wrong answer
        print("Incorrect!")
        print("Game Board")
        life -= 1
        print("[ " + hearts + "]")

print(f"You ran out of lives and are no longer a sentient feline. Though you're now incapable of caring, the word was {secret_word}.")

# # while guessed_word_correctly = False
# #     guess = input("Guess a letter: ")
# #     if guess == ():
# guessed_word_correctly = False

# clue = list("?????")

# heart_symbol = u'\u2764'

# lives = heart_symbol * 9
# print(lives)
# game_board = [["?"], ["?"], ["?"], ["?"], ["?"]]

# # tic_tac_toe = [["X", "X", "X"],
# #                ["X", "O", "X"],
# #                ["X", "X", "O"]]

# print(tic_tac_toe[1][1]) # first index is "row", second index is "column", X and Y coords.
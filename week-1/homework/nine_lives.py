import random

lives = 9

words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]

secret_word = random.choice(words)

secret_word_list = list(secret_word)

print("Guess the secret word. You have nine tries.") # it works up to here

heart_symbol = u'\u2764'
life = 9
lives = heart_symbol * life


while life > 0:
    answer = input("guess a letter: ")
    if answer.lower() == (): #wrong answer
        life -= 1

print(f"You ran out of guesses. The word was {secret_word}.")
        


# while guessed_word_correctly = False
#     guess = input("Guess a letter: ")
#     if guess == ():
guessed_word_correctly = False

clue = list("?????")

heart_symbol = u'\u2764'

lives = heart_symbol * 9
print(lives)
game_board = [["?"], ["?"], ["?"], ["?"], ["?"]]

# tic_tac_toe = [["X", "X", "X"],
#                ["X", "O", "X"],
#                ["X", "X", "O"]]

# print(tic_tac_toe[1][1]) # first index is "row", second index is "column", X x Y coords.
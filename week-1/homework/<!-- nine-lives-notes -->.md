<!-- nine-lives-notes -->

- words
    - holds list of words
    - 5 letters long
- list of clues ["?", "?", "?", "?", "?"]
    - 5 choices
- secret word
    - randomly chosen from word list
- lives = 9
    - decrements every time a letter is guessed incorrectly
- guess
    - value received from user

<!-- gameplay -->

- user guesses a letter
    - input function for user
- code checks to see if letter is in secret_word variable

- if guess is correct
    - we need to loop through each char.
    - find the index of where the guess lies in secret_word
    - replace index in list of clues (?) with correct letter
    - what if there are duplicated letters in word?
- if guess is incorrect
    - lose a heart, lives decremented
    - check to see if user has > 0 lives left
- if full word is guessed
    - print winning statement, display winning word
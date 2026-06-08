
 # 📘 Assignment: Hangman Game Challenge

 ## 🎯 Objective

 Create a command-line Hangman game in Python where the player guesses letters to reveal a hidden word before running out of attempts. Practice string manipulation, loops, conditionals, and user input handling.

 ## 📝 Tasks

 ### 🛠️ Implement the core Hangman game

 #### Description
 Build a terminal-based Hangman game that:
 - Selects a random secret word from a predefined list.
 - Shows the player's progress using underscores for unrevealed letters.
 - Accepts single-letter guesses (case-insensitive) and updates the display.
 - Tracks incorrect guesses and remaining attempts.
 - Handles repeated guesses and invalid input gracefully.

 #### Requirements
 Completed program should:

 - Randomly choose a secret word from a built-in list.
 - Display the current word progress like `_ a _ _ m a n`.
 - Accept single-letter input and update the progress display.
 - Maintain and display the list of guessed letters.
 - Track remaining incorrect attempts (for example, 6 attempts) and decrement on wrong guesses.
 - Terminate when the word is fully guessed or attempts reach zero.
 - Display a clear win or lose message and reveal the secret word.

 #### Example session
 ```
 Secret word: python
 Progress: _ _ _ _ _ _
 Guess a letter: p
 Progress: p _ _ _ _ _
 Guessed letters: p
 Remaining attempts: 6
 ...
 ```

 ### 🛠️ Add enhancements (optional)

 #### Description
 Implement at least two optional features to extend the game experience. Options include:
 - Loading words from an external file (e.g., `assets/words.txt`).
 - Difficulty levels that adjust attempts or word length.
 - Allowing whole-word guesses.
 - ASCII-art hangman that progresses with wrong guesses.
 - Persisting simple stats or high scores to a file.

 #### Requirements
 Completed program should:

 - Implement a working core game (Task 1) plus at least two enhancements from the list.
 - Include brief usage notes in the code or this README explaining how to enable/configure the enhancements.

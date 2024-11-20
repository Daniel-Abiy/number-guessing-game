# Number Guessing Game in Python

## Description
This is a simple number guessing game in Python. The computer randomly selects a number within a given range, and the player has to guess it. The player has 3 chances to guess the correct number, with hints provided after each guess (whether the guess is too high or too low).

## Features
- The user can define a custom range for the random number (start and end values).
- The player has 3 attempts to guess the correct number.
- After each guess, the game provides feedback if the guess is too low or too high.
- The game congratulates the player if they guess correctly within the allowed attempts.

## Requirements
- Python 3.x.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Daniel-Abiy/number-guessing-game/
   ```

2. Navigate to the project folder:

   ```bash
   cd number-guessing-game
   ```

3. Run the number guessing game script:

   ```bash
   python number_guessing_game.py
   ```

## How to Play
1. When prompted, enter the starting and ending values for the range within which the computer will select a random number.
2. The game will then ask you to guess a number.
3. You have 3 chances to guess the number.
4. After each guess, the game will tell you if your guess is too high or too low.
5. If you guess the number correctly within 3 tries, you win; otherwise, the game will inform you that you've used all your chances.

## Example

```
Enter the start of the number: 1
Enter the end of the number: 10
The computer will think of a number between  1 and  10
Enter your guess here: 5
Too Low
TRY AGAIN: 7
Too High
TRY AGAIN: 6
Congratulation you have won the game
```

## Contributing
Feel free to fork the project, make improvements, and submit pull requests.

## License
This project is open-source and available under the MIT License.

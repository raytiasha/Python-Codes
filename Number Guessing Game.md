# Number Guessing Game

A simple command-line Number Guessing Game where the player tries to guess a randomly generated number between **1 and 100**.

## Features

* Randomly generates a number between **1 and 100**.
* Prompts the user to enter a guess.
* Provides hints after each incorrect guess:

  * **Guess Higher** if the guess is too low.
  * **Guess Lower** if the guess is too high.
* Continues until the correct number is guessed.
* Displays the total number of attempts taken to guess the correct number.

## How It Works

1. The game randomly selects a number between **1** and **100**.
2. The player enters a guess.
3. The game compares the guess with the secret number.
4. If the guess is incorrect:

   * The game tells the player to guess **higher** or **lower**.
5. Steps 2–4 repeat until the player guesses the correct number.
6. Once the correct number is guessed, the game displays a congratulatory message along with the total number of attempts.

## Example

```text
Welcome to the Number Guessing Game!

Guess a number between 1 and 100: 50
Guess Higher!

Guess a number between 1 and 100: 75
Guess Lower!

Guess a number between 1 and 100: 63
Guess Higher!

Guess a number between 1 and 100: 68
Congratulations! You guessed the correct number.

Total attempts: 4
```

## Getting Started

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd <project-folder>
```

3. Compile and/or run the program according to the programming language used for your implementation.

## Future Improvements

* Add difficulty levels (Easy, Medium, Hard).
* Limit the number of attempts.
* Display a score based on attempts.
* Allow multiple rounds without restarting the game.
* Maintain a high-score leaderboard.
* Add input validation for invalid or out-of-range values.

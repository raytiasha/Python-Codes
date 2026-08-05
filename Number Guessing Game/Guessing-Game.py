import random

jackpot = random.randint(1, 100)
GuessedNumber = int(input("Guess a number between 1 and 100: "))
count = 1

while GuessedNumber != jackpot:
    count += 1
    if GuessedNumber < jackpot:
        print("Guess a higher number.")
    else:
        print("Guess a lower number.")

    GuessedNumber = int(input("Guess a number between 1 and 100: "))

print(f"Hooray! You've guessed the correct number {jackpot} in {count} attempts.")

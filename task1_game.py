secret_number = 73

guess = 0

while guess != secret_number:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess == secret_number:
        print("Congratulations! You guessed it right.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
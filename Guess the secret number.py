number = 76
print(number)

guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("You guessed the secret number! You win a potato!")
else:
    print("Sorry, that was the wrong number.")
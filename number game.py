import random
playing = True
number = str(random.randint(1, 100))
print("I'm thinking of a number between 1 and 10 can you guess it?")
while playing:
    guess = input("Your guess: ")
    if guess == number:
        print("Congratulations! You guessed the number.")
        playing = False
    else:
        print("Sorry, that's not it. Try again.")57
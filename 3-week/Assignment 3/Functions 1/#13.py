import random
NumberToGuess=random.randint(1,20)

print('Hello! What is your name?')
name = input()
print()
print("Well,", name, "I am thinking of a number between 1 and 20.")
userGuess = -1
while userGuess!=NumberToGuess:
    userGuess = int(input())


    if userGuess > NumberToGuess:
        print('Take a guess')
        print("Your guess is too high")

    elif userGuess < NumberToGuess:
        print('Take a guess')
        print("Your quess is too low. ")

    else:
        print("Good job," ,name, "You guessed my number in "+ str(NumberToGuess))


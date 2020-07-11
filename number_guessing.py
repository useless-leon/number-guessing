import random

hidden = random.randrange(1, 200)
#print(hidden)

guess = int(input("Please enter your guess: "))

if guess == hidden:
    print("Hit!")
elif guess < hidden:
    print("Your guess is too low")
else:
    print("Your guess is too high")
print("The number is " , hidden , "!")
while input("Play Again? (Y/N) ").upper() == "Y":
    guess = int(input("Please enter your guess: "))
    if guess == hidden:
        print("Hit!")
    elif guess < hidden:
        print("Your guess is too low")
        print("The number is " , hidden , "!")
    else:
        print("Your guess is too high")

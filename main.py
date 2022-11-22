import random
print("\n\n-- Welcome to the Number guessing game! --\n\n")

topRangeNumber = input("* Please input a MAX number:  ")

if topRangeNumber.isdigit():
    topRangeNumber = int(topRangeNumber)

    if topRangeNumber <= 0:
        print("Enter a Number higher than 0 ...:")

else:
    print("Please Select a Valid Number: ")
    quit()
randomNumber = random.randint(0, topRangeNumber)

attempt = 0
while True:
    attempt += 1
    userGuess = input("* make a guess: ")

    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Please Select a Valid Number: ")
        continue

    if userGuess == randomNumber:
        print("You are Correct! ...")
        break
    elif userGuess > randomNumber:
        print("  Lower ")
    else:
        print("  Higher ")

print(f"You guessed right in {attempt} attempts !")
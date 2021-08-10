import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Guess the number between 1 to 100: "))
    guesses +=1
    if(userGuess==randNumber):
        print("you guess is right you won")
    else:
        if(userGuess>randNumber):
            print("smaller number please")
        else:
            print("larger number please")

print(f"your number of guesses is {guesses}")

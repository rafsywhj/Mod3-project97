import random;
print("NUMBER GUESSING GAME")

number = random.randint(1,9)

print("GUESS ANY NUMBER BETWEEN 1 AND 9")


chance = 0



while(chance < 5 ):

    guess = int(input("Enter your guess :  "))

    if(number == guess):
        print("CONGRATULATIONS...!!! YOUR GUESS IS CORRECT")
        break

    elif(number < guess):
        print("Guess number lesser than ", guess)

    else:
        print("Guess number greater than ", guess)
    chance += 1


if(chance == 5):
    print("YOU LOSE THIS GAME...!!!! Number is ", number)

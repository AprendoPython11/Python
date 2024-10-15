import random

def guess(y):
    random_number = random.randint(1, y)
    guess = 0

    while(guess != random_number):

        guess = int(input(f"Gess a number between 1 and {y}: "))
        
        if(guess > random_number):
            print("Sorry, It was too high. Try again")
        elif(guess < random_number):
            print("Sorry, It was too low. Could you try again?" )

    print(f"Congratulacion, you did. {random_number} It was the correctly number")


guess(10)
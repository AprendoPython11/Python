import random

# the user guess the random number 
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

# the computer guess the random number 

def computer_guess(y):
    low = 1
    hight = y
    reply = ""
    
    while (reply != "c"):
        number_for_guess = random.randint(low, hight)
        reply = input(f"Is {number_for_guess} too low (l) or too hight(h), or maybe is correct (c)? :")
        
        if(reply == "l"):
            low = number_for_guess + 1
            
        elif(reply == "h"):
            hight = number_for_guess - 1
    
    print("I did! I guess the number {number_for_guess}")
            

guess(10)
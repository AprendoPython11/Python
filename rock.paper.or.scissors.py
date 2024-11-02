import random;

def play():
    user = input("Enter 'r' for rock, 'p' for paper or 's' for sccisors: ")
    computer_response = random.choice(["r", "p", "s"])
    print(f"the reponse od the computer {computer_response}")

    if user == computer_response:
        return "Empatados"
    
    if ganador(user, computer_response):
        return "You won !"
    
    return "You lost !"

def ganador(player, oponent):
    if(player == "s" and oponent == "p" ) or (player == "r" and oponent == "s") or \
    (player == "p" and oponent == "r"):
        return True

print(play())
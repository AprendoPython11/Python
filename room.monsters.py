import random

def game():
    print("Hello, you are in a room, where there two doors, \n in one you will be able to encounter a monter or a treasure")
    player_choose = input("You have to choose one door, \n enter 'A' for the right door or 'B' for the left door. ")
    
    while True:
        if player_choose.lower() in ["a", "b"]:
            break
        else:
            return "This room doesn't exist"

    if treasure_room(player_choose):
        return "Congratulations !You have encountered the Treasure!"
    else:
        monster()
    
    
def treasure_room(x_room):
    x_room = random.choice(["t", "m"])
    print(x_room)

    if x_room == "t":
        return True


def monster():
    x_monster = random.randint(1, 5)

    match x_monster:
        case 1:
            return "You have encountered a level A1 moster"
        case 2:
            return "You have encountered a level B2 monster"
        case 3:
            return "You have encountered a level C3 monster"
        case 4:
            return "You have encountered a level D4 monster"
        case 5:
            return "You have encountered a level E5 mosnter"

print(game())

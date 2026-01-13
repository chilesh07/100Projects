print("Welcome to Treasure Island")
print("Your mission is to find the Treasure 🏴‍☠️🏴‍☠️🏴‍☠️ !!! ")
choice1=input('You are at the cross road.Where do you want to go?\n Type "left" or "right" \n ').lower()
if choice1 == "left":
    choice2 = input('You are come to a lake, there is an island in the middle of the lake.\n "wait" to wait for a boat.Type "swim" to swin across \n').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed.There is a house with 3 doors.One red, one yellow and one blue.which colour do you choose?\n').lower()
        if choice3 == "yellow":
            print("You found the treasure!🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️.You Win!")
        elif choice3 == "red":
            print("It'sroom full of fire🔥🔥🔥🔥🔥🔥.\n Game Over")
        else:
            print("You enter a room of beasts👹👹👹👹👹.\nGame over.")
    else:
        print("Attacked by the shark🦈🦈🦈🦈🦈🦈.\n Game over")
else:    
    print("you hit by a car \n Game Over")
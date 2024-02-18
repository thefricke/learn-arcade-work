import random


def main():
    print("Welcome to Camel")
    print("You have stolen a camel to make your way across the great Mobi desert")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and outrun the natives.")

    # define variables
    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_traveled = -20
    canteen = 3

    while not done:
        print("A. Drink from you canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        user_choice = input("What is your choice? ")

        # game logic follows
        if user_choice.upper() == "Q":
            print("You have quit the game.")
            break
        elif user_choice.upper() == "E":
            print("\nYou have traveled " + str(miles_traveled) + " miles.")
            print("You have " + str(canteen) + " drinks left.")
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you.\n")
        elif user_choice.upper() == "D":
            print("\nYou have stopped for the night to rest.")
            print("Your camel is rested and happy!")
            natives_traveled = natives_traveled + random.randrange(7, 15)
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you.\n")
        elif user_choice.upper() == "C":
            print("\nYour camel runs full speed ahead.")
            miles_traveled = miles_traveled + random.randrange(10, 21)
            camel_tiredness = camel_tiredness + random.randrange(1, 4)
            natives_traveled = natives_traveled + random.randrange(7, 15)
            thirst = thirst + 1
            if not done and random.randrange(1, 21) == 1:
                print("You found an oasis!\n")
                canteen = 3
                thirst = 0
                camel_tiredness = 0
            else:
                print("No oasis in sight.\n")
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you.\n")
        elif user_choice.upper() == "B":
            print("\nYour camel runs at a moderate speed.")
            miles_traveled = miles_traveled + random.randrange(5, 13)
            camel_tiredness = camel_tiredness + 1
            natives_traveled = natives_traveled + random.randrange(7, 15)
            thirst = thirst + 1
            if not done and random.randrange(1, 21) == 1:
                print("You found an oasis!\n")
                canteen = 3
                thirst = 0
                camel_tiredness = 0
            else:
                print("No oasis in sight.\n")
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you.\n")
        elif user_choice.upper() == "A":
            if canteen > 0:
                thirst = 0
                canteen = canteen - 1
                print("\nYou drink from your canteen.")
            else:
                print("\nYou have no drinks left.")
            print("The natives are " + str(miles_traveled - natives_traveled) + " miles behind you.\n")

        if thirst > 6:
            print("You died of thirst!\n")
            break
        elif thirst > 4:
            print("You are thirsty!.\n")

        if camel_tiredness > 8:
            print("Your camel died of exhaustion!\n")
            break
        elif camel_tiredness > 5:
            print("Your camel is getting tired!.\n")

        if miles_traveled - natives_traveled <= 0:
            print("The natives have caught you, game over.\n")
            break
        elif miles_traveled - natives_traveled < 15:
            print("The natives are getting close!\n")

        if not done and miles_traveled >= 200:
            print("You win!\n")
            break

main()

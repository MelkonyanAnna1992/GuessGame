# Modify the program below to use a while loop to allow as many guesses as necessary.

#  The program should let the player know whether to guess higher or lower, 
# and should print a message when the guess is correct. A correct guess 
# will terminate the program.

#   As an optional extra , allow the player to quit by entering 0 (zero)
# for their guess.

import time
import random


#--------------------------------------------------------------------
# This function includes
#  the whole logic of the game
#--------------------------------------------------------------------
def guessGame():

    print("-"*50)
    try:
        v_lowest = int(input("   Please write the lowest guess value in \n   integer format -> "))
    except ValueError:
        v_lowest = 1
        print("_"*50)
        print("   Lowest value for guess setted incoorect\n \t\tDefault value is 1")
        print("_"*50)
    print("-"*50)
    print("-"*50)
    try:
        v_highest = int(input("   Please write the highest guess value in \n   integer format -> "))
    except ValueError:
        v_highest = 10
        print("_"*50)
        print("   Highest value for guess setted incoorect\n \t\tDefault value is 10")
        print("_"*50)
    print("-"*50)

    if v_lowest == v_highest:
        v_highest += 5
    elif v_lowest > v_highest:
        v_highest, v_lowest = v_lowest, v_highest
    v_answer = random.randint(v_lowest, v_highest)

    print("-"*50)
    print("   Please guess a number (in integer format) \n\t\tbetween {} and {}:".format(v_lowest, v_highest))

    try:
        v_guess = int(input("   \t\t\t"))
    except ValueError:
        v_guess = 3
        print("_"*50)
        print("        Value for guess setted incoorect\n \t\tDefault value is 3")
        print("_"*50)
    print("-"*50)
    if v_guess != v_answer:
        if v_guess < v_answer:
            print("-"*50)
            print("   \t\tPlease guess higher")
            try:
                v_guess = int(input("   \t\t\t"))
            except ValueError:
                v_guess = 7
                print("_"*50)
                print("   Higher value for guess setted incoorect\n \t\tDefault value is 7")
                print("_"*50)
            print("-"*50)
        else: # guess must be greater than number
            print("-"*50)
            print("   \t\tPlease guess lower")
            try:
                v_guess = int(input("   \t\t\t"))
            except ValueError: 
                v_guess = 2
                print("_"*50)
                print("     Lower value for guess setted incoorect\n \t\tDefault value is 2")
                print("_"*50)
            print("-"*50)
        if v_guess == v_answer:
            print("\t   Well done, you guessed it.\n\n\t        YOU ARE WIN !!!\n")
            print("\t\tToday WINNER is \n\t\t{} {}".format(v_name, v_surname))
        else:
            print("_"*50)
            print("   Sorry, you have not guessed correctly.")
            print("   The guested value was -> ", v_answer)
            print("_"*50)
    else:
        print("\t   Well done, you guessed it.\n\n\t        YOU ARE WIN !!!\n\t          $100000000000\n")
        print("\t\t Today WINNER is \n\t\t   {} {}".format(v_name, v_surname))
    
    return

print("^"*50)
print("\t\t      START ")
print("*"*50)
print("   Welcome to Anna Melkonyan's GAME !!!  ")
print("   Please register your Name and Surname")
print("-"*50)
v_name = input("   Please write your Name -> ")
print("   Your name was accepted.  ")
print("-"*50)
v_surname = input("   Please write your Surname -> ")
print("   Your surname was accepted.  ")
print("-"*50)
print("="*50)
print("   Welcome to the GAME Dear {}, \n   We are lucky to see you on this game.  ".format(v_name))
print("="*50)
v_false_count = 0

while True:
    print("#"*50)
    print("   \n\t\tAre you ready?\n ")
    print("   If 'YES', please click on 'y' or 'Y' button")
    print("   If 'NO', please click on 'n' or 'N' button.  ")
    v_ready = input()
    if v_false_count > 3:
        print("-"*50)
        print("Program terminated. Multyple wrong button clicked.")
        print("\t    Please restart the program.")
        print("-"*50)
        break
    else:
        if v_ready in ('y', 'Y'):
            print("="*50)
            print("\t\t    GREAT !!! \n\n   \t\tLet's start the game \n\t\tDear {} {}".format(v_name, v_surname))
            print("="*50)
            print("^"*50)
            print("   \tPlease wait\n\tProgram is loading ...")
            print("^"*50)
            time.sleep(7)
            guessGame()
            break
        elif v_ready in ('n', 'N'):
            print("="*50)
            print("   \t\tNo problem \n".format(v_name, v_surname))
            print("   \t   Be ready in the next time.  ")
            print("   \t\tWill see you soon  ")
            print("   \t\tDear {} {} \n   \t\t     Bye".format(v_name, v_surname))
            print("="*50)
            break
        else:
            v_false_count += 1
            print("-"*50)
            print("   Please click ONLY 'y', 'Y' or 'n', 'N' button. ")
            print("   You have only {} times for correct click.".format(5-v_false_count))
            print("-"*50)

    print("#"*50)

print("*"*50)
print("      \t\t\tEND ")
print("^"*50)


# v_lowest = int(input("Please insert a lowest namber for game"))
# v_highest = 10
# v_answer = random.randint(1, v_highest)

# print("*"*10)
# print(v_answer)
# print("*"*10)

# print("Please guess a number between 1 and {}:".format(v_highest))
# guess = int(input())
# if guess != v_answer:
#     if guess < v_answer:
#         print("Please guess higher")
#     else: # guess must be greater than number
#         print("Please guess lower")
#     guess = int(input())
#     if guess == v_answer:
#         print("Well done, you guessed it")
#     else:
#          print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

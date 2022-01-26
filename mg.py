import random


def bat():
    """ove = int(ov * 6)
    r = 1"""
    print("\n\nYou are now batting!")
    your_score = 0
    while 1:
        shot = int(input("Your move: \t"))
        bowl = random.randint(0, 6)
        print("\nComputer's move: " + str(bowl))
        if (shot != 0) and (shot != 1) and (shot != 2) and (shot != 3) and (shot != 4) and (shot != 5) and (shot != 6):
            print("Enter a valid move: ")
            continue
        if shot == bowl:
            print("OUT!!!\nYour score: " + str(your_score))
            break
        if shot != 0 and bowl == 0:
            your_score += shot + 1
            print("Computer committed a No-Ball\nFREE HIT!!!")
            shot = int(input("Your extra move: \t"))
            bowl = random.randint(0, 6)
            print("\nComputer's extra move: " + str(bowl))
            if shot == bowl:
                print("Sneaky, it could be a wicket if it were not a free-hit")
            else:
                your_score += shot
            print("Your score: " + str(your_score))
        else:
            your_score += shot
            print("Your score: " + str(your_score))
        """if r % 6 == 0:
            print(str(int(r / 6)) + "th Over Ends")
        if r == ove:
            print("INNINGS OVER!")
            break
        r += 1"""
    return your_score


def field():
    """ove = int(ov * 6)
    r = 1"""
    print("\n\nComputer is now batting!")
    comp_score = 0
    while 1:
        bowl = int(input("Your move: \t"))
        shot = random.randint(0, 6)
        print("\nComputer's move: " + str(shot))
        if (bowl != 0) and (bowl != 1) and (bowl != 2) and (bowl != 3) and (bowl != 4) and (bowl != 5) and (bowl != 6):
            print("Enter a valid move: ")
            continue
        if shot == bowl:
            print("OUT!!!\nComputer's score: " + str(comp_score))
            break
        if shot != 0 and bowl == 0:
            comp_score += shot + 1
            print("You committed a No-Ball\nFREE HIT!!!")
            bowl = int(input("Your extra move: \t"))
            shot = random.randint(0, 6)
            print("\nComputer's extra move: " + str(shot))
            if shot == bowl:
                print("Sneaky, it could be a wicket if it were not a free-hit")
            else:
                comp_score += shot
            print("Computer's score: " + str(comp_score))
        else:
            comp_score += shot
            print("Computer's score: " + str(comp_score))
        """if r % 6 == 0:
            print(str(int(r / 6)) + "th Over Ends")
        if r == ove:
            print("INNINGS OVER!")
            break
        r += 1"""
    return comp_score


def toss():
    p = 1
    # procedure of tossing via rock paper scissors(an infinite loop)
    while 1:
        i = int(input("\nEnter 1 for Rock.\nEnter 2 for Scissors.\nEnter 3 for Paper.\n"))  # your choice
        n = random.randint(1, 3)  # computer's choice
        if n == 1:
            print("\nComputer drew Rock.")
        if n == 2:
            print("\nComputer drew Scissors.")
        if n == 3:
            print("\nComputer drew Paper.")
        if i == n:
            print("\nToss again.\n")
            continue
        if (i != 1) and (i != 2) and (i != 3):
            print("\nEnter a valid move: \n")
            continue
        if i != n:
            # user wins the toss  V
            if (i == 1 and n == 2) or (i == 2 and n == 3) or (i == 3 and n == 1):
                p = 1
            # computer wins the toss   V
            else:
                p = 2
            break
    if p == 2:
        # computer deciding to either field or bat first
        choice = random.randint(1, 2)
        if choice == 2:
            print("Computer won the toss and decided to bat first.")
        else:
            print("Computer won the toss and decided to field first.")
    if p == 1:
        # your decision
        print("You won the toss.")
        while 1:
            choice = int(input("Choose 1 to bat first.\nChoose 2 to field first.\n"))
            if (choice != 1) and (choice != 2):
                print("Enter a valid option: \n")
                continue
            if choice == 1:
                print("You won the toss and decided to bat first.")
                break
            if choice == 2:
                print("You won the toss and decided to field first.")
                break
    return choice


def play_now():
    """while 1:
        ov = int(input("How many overs will you want to play?\t " + name + "\n"))
        if ov == 0:
            print("Please play at least '1' over.")
            continue
        else:
            break"""
    print("\n\nTOSS TIME...")
    print("\n*****For toss we will play a game of rock, paper, scissors*****\n")
    c = toss()
    if c == 1:
        ur_sc = bat()
        com_sc = field()
    else:
        com_sc = field()
        ur_sc = bat()
    if com_sc == ur_sc:
        print("GAME TIED!")
    if com_sc > ur_sc:
        print("You lost the game : (")
    if com_sc < ur_sc:
        print("Hurray! You won the game! : D")
    

def rules():
    print("It is a very casual imitation of the real life cricket.\nYou can choose from 7 preset moves (0-6). "
          "If the moves of both the player matches, then the player who is batting is declared out.\nThis doesn't "
          "happen only in the case of a no-ball.\nThus following a free hit.\n"
          "No-Ball happens when bowler plays zero but the batsman doesn't. Out during free-hit is declared a dot."
          "\n\n\nNERDY STATS:\n6/7 probability to score runs. 1/7 probability to take a wicket\n"
          "So, it is easier to score runs if you're not very unlucky (unfavourable outcomes)"
          "\n\n\n\n\n\t\tTHE GAME PRESENTLY DOESN'T INVOLVE THE FEATURE TO PLAY USER "
          "DEFINED OVERS. \n\t\tALSO THE CHASE ISN'T FIXED. IT SHALL BE FIXED IN THE FUTURE UPDATES!\nThank You!! ")


# return s


def about():
    print("\t\t\t******ABOUT******\n")
    print("WHC- WORLD OF HAND CRICKET\nWelcome player\nThis game is based on real Hand Cricket Strategies.")
    print("Heavily dependent on probability: you can choose from 7 preset moves...\n\n")
    print("ENJOY\n@Copyrights reserved\n")
    print("Choose again")


"""def choose(a):
    d = {1: play_now(), 2: rules(), }
    return d.get(a, about())"""


print("\t\t\t*****Welcome to the world of Hand Cricket*****")
name = str(input("\n\nEnter your name: "))
print("\nWELCOME\t" + name + "!!!!")
print("\n\n******** GAME MENU ********")
print("\n'1' - Play now!\n'2' - How to Play ")
ar = int(input("Enter:\t"))
# print(choose(ar))
if ar == 1:
    play_now()
if ar == 2:
    rules()
# if ar != 1 and ar != 2:
#     about()
else:
    about()

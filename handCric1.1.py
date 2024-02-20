import random as r


class helper:
    def toss(self):
        rpc = None
        # procedure of tossing via rock paper scissors(an infinite loop)
        while True:
            # your choice
            i = int(input("\nEnter 1 for Rock.\nEnter 2 for Scissors.\nEnter 3 for Paper.\n")) 
            if i not in range(1, 4):
                print("\nInvalid move... \n")
                i = r.randint(1, 3)
                if i == 1:
                    print("RNG drew Rock.")
                if i == 2:
                    print("RNG drew Scissors.")
                if i == 3:
                    print("RNG drew Paper.")
            n = r.randint(1, 3)  # computer's choice
            if n == 1:
                print("\nComputer drew Rock.")
            if n == 2:
                print("\nComputer drew Scissors.")
            if n == 3:
                print("\nComputer drew Paper.")
            if i == n:
                print("\nToss again.\n")
                continue
            if i != n:
                if (i == 1 and n == 2) or (i == 2 and n == 3) or (i == 3 and n == 1):
                    rpc = "User_won_toss"
                else:
                    rpc = "Comp_won_toss"
                break
        if rpc == "Comp_won_toss":
            # computer deciding to either field or bat first
            choice = r.randint(1, 2)
            if choice == 2:
                choice = "User_fields_first"
                print("Computer won the toss and decided to bat first.")
            else:
                choice = "User_bats_first"
                print("Computer won the toss and decided to field first.")
        if rpc == "User_won_toss":
            # your decision
            print("You won the toss.")
            while True:
                choice = int(input("Choose 1 to bat first.\nChoose 2 to field first.\n"))
                if (choice != 1) and (choice != 2):
                    print("Invalid option: (rng_used) \n")
                    choice = r.randint(1, 2)
                if choice == 1:
                    choice = "User_bats_first"
                    print("You won the toss and decided to bat first.")
                    break
                if choice == 2:
                    choice = "User_fields_first"
                    print("You won the toss and decided to field first.")
                    break
        return choice

    def bat(self, com_sc, over):
        print("\n\nYou are now batting!")
        your_score = 0
        for i in range(1, (over*6)+1):
            shot = int(input("\nYour move: \t"))
            bowl = r.randint(0, 6)
            print("\nComputer's move: " + str(bowl))
            if shot not in range(0, 7):
                print("Invalid move: ")
                shot = r.randint(0, 6)
            if shot == bowl:
                print("OUT!!!\nYour score: " + str(your_score))
                break
            if shot != 0 and bowl == 0:
                your_score += shot + 1
                print("Your score: " + str(your_score))
                print("Computer committed a No-Ball\nFREE HIT!!!")
                shot = int(input("Your extra move: \t"))
                if shot not in range(0, 7):
                    print("Invalid move... ")
                    shot = r.randint(0, 6)
                bowl = r.randint(0, 6)
                print(f"\nComputer's extra move: {str(bowl)}")
                if shot == bowl:
                    print("Sneaky, it could be a wicket if it were not a free-hit")
                else:
                    your_score += shot
                print("Your score: " + str(your_score))
            else:
                your_score += shot
                print("Your score: " + str(your_score))
            if com_sc != "1st_innings" and your_score > com_sc:
                break
            if i%6 == 0:
                print(f"{i//6}th over has ended.")
        return your_score
    
    def field(self, ur_sc, over):
        print("\n\nComputer is now batting!")
        comp_score = 0
        for i in range(1, (over*6)+1):
            bowl = int(input("Your move: \t"))
            shot = r.randint(0, 6)
            print("\nComputer's move: " + str(shot))
            if bowl not in range(0, 7):
                print("Invalid move... ")
                bowl = r.randint(0, 6)
            if shot == bowl:
                print("OUT!!!\nComputer's score: " + str(comp_score))
                break
            if shot != 0 and bowl == 0:
                comp_score += shot + 1
                print("You committed a No-Ball\nFREE HIT!!!")
                print("Computer's score: " + str(comp_score))
                bowl = int(input("Your extra move: \t"))
                if bowl not in range(0, 7):
                    print("Invalid move...")
                    bowl = r.randint(0, 6)
                shot = r.randint(0, 6)
                print("\nComputer's extra move: " + str(shot))
                if shot == bowl:
                    print("Sneaky, it could be a wicket if it were not a free-hit")
                else:
                    comp_score += shot
                print("Computer's score: " + str(comp_score))
            else:
                comp_score += shot
                print("Computer's score: " + str(comp_score))
            if ur_sc != "1st_innings" and comp_score > ur_sc:
                break
            if i%6 == 0:
                print(f"{i//6}th over has ended.")
        return comp_score


class handCric:
    def rules(self):
        print("It is a very casual imitation of the real life cricket.\n\n>> Toss of the game is "
              "done by Rock-Papper-Scissors.\n>> During the play you can choose from "
              "7 preset moves (0-6). If the moves of both the player matches, then the player" 
              " who is batting is declared out.\n>> This doesn't happen only in the case of a no-ball,"
              " therefore following a free hit.\n>> No-Ball happens when bowler plays zero but the "
              "batsman doesn't. Out during free-hit is declared a dot.\n>> Invalid move from the user"
              "is replaced by a rng(random-number-generator) mechanic.\n\n\nNERDY STATS:"
              "\n6/7 probability to score runs. 1/7 probability to take a wicket\n"
              "So, it is easier to score runs if you're not very unlucky (unfavourable outcomes)"
              "\n\n\n\n\n\t\tFEATURE TO PLAY USER DEFINED OVERS ADDED, INFINITE-CHASE ISSUE FIXED "
              " \n\t\t FURTHER Q.O.L. AND UI TO BE ADDED IN THE FUTURE" 
              "UPDATES!\nThank You!! ")

    def play_now(self):
        print("\nSelect, how many overs you wish to play.\n"
              "1(minimum/default), 50(maximum)")
        over = int(input())
        if over < 1 or over > 50:
            over = 1
        print("\n\nTOSS TIME..."
              "\n*****For toss we will play a game of rock, paper, scissors*****\n")
        utility = helper()
        c = utility.toss()
        if c == "User_bats_first":
            ur_sc = utility.bat("1st_innings", over)
            com_sc = utility.field(ur_sc, over)
        else:
            com_sc = utility.field("1st_innings", over)
            ur_sc = utility.bat(com_sc, over)
        if com_sc == ur_sc:
            print("GAME TIED!")
        if com_sc > ur_sc:
            print("You lost the game : (")
        if com_sc < ur_sc:
            print("Hurray! You won the game! : D")
    
    def about(self):
        print("\t\t\t******ABOUT******\n"
              "WHC- WORLD OF HAND CRICKET\nWelcome player\n"
              "This game is based on real Hand Cricket Strategies."
              "Heavily dependent on probability: you can choose from 7 preset moves...\n\n"
              "ENJOY\n@Copyrights reserved\n"
              "Play again later")


def welcome():
    print("\n\t\t\t*****Welcome to the world of Hand Cricket*****")
    name = str(input("\nEnter your name: "))
    print("\nWELCOME\t" + name + "!!!!")
    print("\n\n******** GAME MENU ********")
    print("\n'1' - Play now!\n'2' - How to Play ")
    ar = int(input("Enter:\t"))
    return [name, ar]


def main():
    name, ar = welcome()
    game = handCric()
    if ar == 1:
        game.play_now()
    elif ar == 2:
        game.rules()
    else:
        game.about()


if __name__ == "__main__":
    main()

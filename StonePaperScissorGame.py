import random
import time

print('Winning rules of the game STONE PAPER SCISSORS are :\n'
      + "Stone vs Paper -> Paper wins \n"
      + "Stone vs Scissors -> Stone wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("lets start the game! \n choose any one of these \n 1-STONE \n 2-PAPER \n 3-SCISSOR")
    choice=int(input("Enter your choice: "))

    while choice>3 or choice<1:
        choice=int(input("you have entered invalid number"))

    if choice==1:
        choice_name='Stone'
    elif choice==2:
        choice_name='Paper'
    else:
        choice_name='Scissor'

    print("your choice is",choice_name)
    print("Now its computer turn...")
    time.sleep(3)

    comp_choice=random.randint(1,3)

    while comp_choice==choice:
        comp_choice=random.randint(1,3)

    if comp_choice==1:
        comp_choice_name='Stone'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissor'

    print("computer choice is",comp_choice_name)
    print(choice_name, "Vs" ,comp_choice_name)

    if choice_name==comp_choice:
        print("Draw")
        result ="Draw"

    if (choice == 1 and comp_choice == 2):
        print('paper wins', end="")
        result = 'paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Stone wins \n', end="")
        result = 'Stone'
    elif (choice == 3 and comp_choice == 1):
        print('Stone wins \n', end="")
        result = 'Stone'

    if (choice == 2 and comp_choice == 3):
        print('Scissor wins', end="")
        result = 'Scissor'
    elif (choice == 3 and comp_choice == 2):
        print('Scissor wins', end="")
        result = 'Scissor'

    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (yes/no)")

    ans = input()
    if ans =='no':
      break

print("Thanks for playing!!!")





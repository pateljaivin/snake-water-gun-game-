import random


def game(comp, you):
    if(comp == you):
        print("the game is tie")

    elif(comp == "s"):
        if(you == "w"):
            print(f" sorry {name}....the computer is win\n")
        elif(you == "g"):
            print(f"{name} is the winner\n")

    elif(comp == "w"):
        if(you == "s"):
            print(f"{name} is the winner\n")
        elif(you == "g"):
            print(f"sorry {name}.....the computer is win\n")

    elif(comp == "g"):
        if(you == "s"):
            print(f"sorry {name}....the computer is win\n")
        elif(you == "w"):
            print(f"{name} is the winner\n")


rand = random.randint(1, 3)

if(rand == 1):
    comp = "s"
elif(rand == 2):
    comp = "w"
else:
    comp = "g"

name = input("please enter your name ::\n")

you = input(f''' {name}'s turn 
            select as for sign
            snake = s
            water = w
            gun = g\n''')

print(f"{name} select the {you}\n")
print('''computer's turn\n''')
print(f"computer select the {comp}\n")
game(comp, you)

import random
def game():
    print('''1 is for Rock
2 is for Paper
3 is for Sissor''')
    com=random.choice([1,2,3])
    player=int(input("Enter your choice: "))
    dic={   
        1:"Rock",
        2:"Paper",
        3:"Scissor",
    }
    if(player>3 or player<1):
        print("Enter correct choice")
        return
    print("Computer choses",dic[com])
    print(f"You choses {dic[player]}")
    if(com==player):
        print("Tie")
    elif(com==1 and player==2):
        print("Player won")
    elif(com==1 and player==3):
        print("Computer won")
    elif(com==2 and player==1):
        print("Computer won")
    elif(com==2 and player==3):
        print("Player won")
    elif(com==3 and player==1):
        print("Player won")
    else:
        print("Computer won")

game()



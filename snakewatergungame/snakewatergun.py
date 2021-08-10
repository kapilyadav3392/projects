import random


def game(comp,you):
    if comp==you:
        return None
    elif you=="s" and comp=="w":
        return True
    elif you=="g" and comp=="s":
        return True
    elif you=="w" and comp=="g":
        return True
    else:
        return False
    
    


print("comp choose Sneak[s], Water[w],Gun(g)?")
randno= random.randint(1,3)

if randno==1:
    comp="s"
elif randno==2:
    comp="w"
elif randno==3:
    comp="g"


you= input("your turn choose Sneak[s], Water[w],Gun(g)?: ")

a=game(comp,you)

if a==None:
        print("the game is tie!")
elif a==True:
        print("you win!")
else:
        print("you lose!")
    
print(f"comp choose {comp}")

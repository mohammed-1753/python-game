import random
"""
0 for gun
1 for rock
-1 for no weapon
"""
computer = random.choice([0,1,-1])
youstr=input("Enter your choice: ") #0 for gun, 1 for rock, -1 for no weapon enter g or r or n
youdict={"Stone":0,"Paper":1,"Scissors":-1}
reversedict={0:"Stone", 1:"Paper", -1:"Scissors"}
you = youdict[youstr]   
print(f"you choose {reversedict[you]} \n computer choose {reversedict[computer]}")

if(you==computer):
    print("it's a draw")

else:
    if(you==0 and computer==1):
        print("you won")
    
    elif(you==0 and computer==-1):
        print("you won")

    elif(you==1 and computer==0):
        print("you lost")

    elif(you==-1 and computer==0):
        print("you lost")

    elif(computer==1 and you==-1):
        print("you lost")

    elif(you==1 and computer==-1):
        print("you won")
    else:
        print("something went wrong")
    
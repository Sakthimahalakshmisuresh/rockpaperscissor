import random
import sys
from enum import Enum

class rps(Enum):
    ROCK=1
    PAPER=2
    SCISSOR=3



print("\n")
playerchoice=input("enter ....\n1 for rock\n2 for paper\n3 for Scissors \n\n")
#print(playerchoice)
# print(type(playerchoice))

player=int(playerchoice)

if player < 1 or player > 3:
    sys.exit("you must enter 1,2 or 3.")

computerchoice=random.choice("123")
computer=int(computerchoice)

print("")
print("you chose "+str(rps(player)).replace('rps.','')+'.')
print("python chose "+str(rps(computer)).replace('rps.','')+'.')
print("")

if player == 1 and computer==3:
    print("you win👌👌\n")
elif player==2 and computer==1:
    print("you win👌👌\n")
elif player==3 and computer==2:
    print("you win👌👌\n")
elif player==computer:
    print("match tie game😑😑")    
else:
    print("python wins !🐍")
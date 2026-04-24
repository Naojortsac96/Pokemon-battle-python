
from random import randint
import os
pikachu_initial_hp=80
squirtle_initial_hp=90

hp_bar=10


pikachu_hp=pikachu_initial_hp
squirtle_hp=squirtle_initial_hp

while pikachu_hp>0 and squirtle_hp>0:
    os.system("cls")

    #The battle begins
    #Pikachu's turn
    print("Pikachu's turn")
    pikachu_attack=randint(1,3)

    filled=int(squirtle_hp/squirtle_initial_hp*hp_bar)
    filled2=int(pikachu_hp/ pikachu_initial_hp*hp_bar)

    if pikachu_attack==1:
        #Thunderbolt
        print("The foe's PIKACHU used Thunderbolt")
        squirtle_hp = max(squirtle_hp - 10, 0)


    elif pikachu_attack==2:
        #Iron Tail
        print("The foe's PIKACHU used Iron Tail")
        squirtle_hp = max(squirtle_hp - 11, 0)

    elif pikachu_attack==3:
        #Thunder Wave
        print("The foe's PIKACHU used Thunder Wave")
        squirtle_hp = max(squirtle_hp - 12, 0)


    filled = int(squirtle_hp / squirtle_initial_hp * hp_bar)
    filled2 = int(pikachu_hp / pikachu_initial_hp * hp_bar)

    print("PIKACHU  HP:[{}]{}/{}\n"
          "SQUIRTLE HP:[{}]{}/{}\n".format("*"*filled2+" "*(hp_bar-filled2),
                               pikachu_hp,pikachu_initial_hp,
                               "*"*filled+" "*(hp_bar-filled),
                               squirtle_hp,squirtle_initial_hp))
    if squirtle_hp==0:
        filled=0
        break


    #Squirtle's turn
    squirtle_attack=None
    while squirtle_attack!="A" and squirtle_attack!="B" and squirtle_attack!="C":
        squirtle_attack=input("What will Squirtle do?\n"
          "[A]Tackle\n"
          "[B]Tail Whip\n"
          "[C]Water Gun\n").upper()
    if squirtle_attack=="A":
        print("Squirtle used Tackle!")
        pikachu_hp=max(pikachu_hp-8,0)
    elif squirtle_attack=="B":
        print("Squirtle used Tail Whip!")
        pikachu_hp = max(pikachu_hp - 11, 0)
    elif squirtle_attack=="C":
        print("Squirtle used Water Gun!")
        pikachu_hp = max(pikachu_hp - 12, 0)

    filled = int(squirtle_hp / squirtle_initial_hp * hp_bar)
    filled2 = int(pikachu_hp / pikachu_initial_hp * hp_bar)

    if pikachu_hp==0:
        filled2=0

    os.system("cls")
    print("Squirtle's turn")

    print("PIKACHU  HP:[{}]{}/{}\n"
          "SQUIRTLE HP:[{}]{}/{}\n".format("*"*filled2+" "*(hp_bar-filled2),
                               pikachu_hp,pikachu_initial_hp,
                               "*"*filled+" "*(hp_bar-filled),
                               squirtle_hp,squirtle_initial_hp))

os.system("cls")
if pikachu_hp>squirtle_hp:
    print("PIKACHU wins!!")

else:
    print("SQUIRTLE wins!")


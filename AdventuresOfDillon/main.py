#Give enemies classes + specials

from random import randint
import player as playa
import enemy1 as bigboypants
import weapons as wepawn
import locations as laca
import json

choseLocation1 = False
choseClass = False
answer1 = False
answer2 = False
specialAttack = False
blockGameWinner = False
Lost = False

while Lost == False:
    sword = wepawn.weapon("Starter Sword", "Sword", 7, 100, None, False, "Starter", "Start", False)
    staff = wepawn.weapon("Starter Staff", "Staff", 7, 100, None, False, "Starter", "Start", False)
    dagger = wepawn.weapon("Starter Dagger", "Dagger", 7, 100, None, False, "Starter", "Start", False)
    bow = wepawn.weapon("Starter Bow", "Bow", 7, 100, None, False, "Starter", "Start", False)

    print('Welcome to the Adventures of Dillon. First we need you to pick a class.')
    print('The classes are Berserk: Where you get a sword that does 30 damage, 5 speed, and an ability that lets you deal 2x damage for 3 turns.')
    print('Mage: Where you get a staff that does 25 damage, 10 speed, and an ability that lets you set the enemy on fire, dealing 5 damage until either them or you are dead.')
    print('Rogue: Where you get a dagger that does 15 damage, 45 speed, and an ability that lets you dodge the enemy attacks')
    print('Archer: Where you get a bow that does 20 damage, 8 speed, and an ability that lets you shot 2 arrows at once with your bow fully charged back')
    print("The speed gives a chance for a double attack for all of the classes except rogue does a triple attack")

    while choseClass == False:
        classInt = int(input('So what will it be. 1 for Berserk, 2 for Mage, 3 for rogue, or 4 for archer '))
        if classInt == 1:
            player = playa.player("Berserk", "GO BERSERK", 5, 30, sword, 160, None, False)
            choseClass = True
        elif classInt == 2:
            player = playa.player("Mage", "Fire", 10, 25, staff, 150, None, False)
            choseClass = True
        elif classInt == 3:
            player = playa.player("Rogue", "Avoid Attack", 45, 15, dagger, 125, None, False)
            choseClass = True
        elif classInt == 4:
            player = playa.player("Archer", "double shot at full charge", 5, 20, bow, 165, None, False)
            choseClass = True
        else:
            print("That is not an option.")

    print("You encounter your first boss. You can click: \n1 to attack,\n2 to block, \n3 to use an item, \n4 to attempt to run.")
    print("The way the block works is that it takes you to a guessing game. If you lose, then you lose your turn but if you win, you deflect the enemy's attack to hit themselves.")
    enemy1 = bigboypants.enemy1("Eldredge Dragon", 10, 300)

    while not answer1:
        while not answer2:
            answer = int(input('What shall you do? '))
            if answer == 1:
                enemy1.health = player.attackMath(enemy1.health, specialAttack)
                answer2 = True
            elif answer == 2:   
                if enemy1.blockGame():
                    #Player won
                    enemy1.health -= 30
                    print("The enemy has been hit for 30 damage and is not at", enemy1.health)
                    blockGameWinner = True
                else:
                    #Player lost
                    blockGameWinner = False
                answer2 = True 
            elif answer == 3:
                answer2 = True
            elif answer == 4:
                print('You failed to run and lost your turn.')
                answer2 = True
            else:   
                print('This is not an option')
        if enemy1.health <= 0:
            answer1 = True
            break
        
        if player.specialMove(enemy1.health, specialAttack) == 1:
            player.health = enemy1.enemyAttack(player.health)
        elif blockGameWinner == False:
            player.health = enemy1.enemyAttack(player.health)
            
        if player.health <= 0:
            Lost = True
            answer1 = True
            break
        else:
            answer2 = False
        
    #First boss done + On to beach
    print("Alright looks light you are moving on from the first boss.")
    print("You will now leave the starter tower.")
    while choseLocation1 == False:
        print("If you would like to enter the beach click 1 or the next boss's room click 2?")
        location1 = int(input("The beach will help you get more gear and items but if you skip to the boss then you will most likely die "))
        if location1 == 1:
            print("Good choice. You will now enter the beach.")
            room1 = laca.room("Beach room 1", 150, 7, 7)
            choseLocation1 = True

        elif location1 == 2:
            print("Ok. Sending you to the boss room")
            choseLocation1 = True

        else:
            print("That is not an option.")




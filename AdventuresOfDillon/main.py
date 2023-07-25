# Import required modules
from random import randint
import player as playa
import enemy1 as bigboypants
import weapons as wepawn
import locations as laca
import json

# Initialize variables
choseLocation1 = False
choseClass = False
answer1 = False
answer2 = False
specialAttack = False
blockGameWinner = False
Lost = False

# Main game loop
while Lost == False:
    # Create starter weapons
    sword = wepawn.weapon("Starter Axe", "Axe", 7, 100, None, False, "Starter", "Start", False)
    staff = wepawn.weapon("Starter Staff", "Staff", 7, 100, None, False, "Starter", "Start", False)
    dagger = wepawn.weapon("Starter Dagger", "Dagger", 7, 100, None, False, "Starter", "Start", False)
    bow = wepawn.weapon("Starter Bow", "Bow", 7, 100, None, False, "Starter", "Start", False)

    # Display class options to the user
    print('Welcome to the Adventures of Dillon. First we need you to pick a class.')
    print('The classes are Berserk: Where you get a sword that does 30 damage, 5 speed, have starter health of 160, and an ability that lets you deal 2x damage for 3 turns.')
    print('Mage: Where you get a staff that does 25 damage, 10 speed, have starter health of 140, and an ability that lets you set the enemy on fire, dealing 5 damage until either them or you are dead.')
    print('Rogue: Where you get a dagger that does 15 damage, 45 speed, have starter health of 130, and an ability that lets you dodge the enemy attacks')
    print('Archer: Where you get a bow that does 20 damage, 8 speed, have starter health of 150, and an ability that lets you shot 2 arrows at once with your bow fully charged back')

    # Class selection loop
    while choseClass == False:
        classInt = int(input('So what will it be. 1 for Berserk, 2 for Mage, 3 for rogue, or 4 for archer '))
        if classInt in [1, 2, 3, 4]:
            # Create player object based on user's class choice
            if classInt == 1:
                #Chose Berserk
                player = playa.player("Berserk", "GO BERSERK", 5, 30, sword, 160, None)
            elif classInt == 2:
                #Chose Mage
                player = playa.player("Mage", "Lengthy Fire", 10, 25, sword, 140, None)
            elif classInt == 3:
                #Chose Rogue
                player = playa.player("Rogue", "Attack dodge", 45, 15, sword, 130, None)
            else:
                #Chose archer
                player = playa.player("Archer", "Double shot", 20, 8, sword, 150, None)
            choseClass = True
        else:
            print("That is not an option.")

    # Display encounter message
    print("You encounter your first boss. You can click: \n1 to attack,\n2 to block, \n3 to use an item, \n4 to attempt to run.")

    # Create enemy object
    enemy1 = bigboypants.enemy1("Eldredge Dragon", 10, 300)

    # Player's turn loop
    while not answer1:
        # Player's action selection loop
        while not answer2:
            answer = int(input('What shall you do? '))
            if answer == 1:
                # Player chooses to attack
                enemy1.health = player.attackMath(enemy1.health, specialAttack)
                answer2 = True
            elif answer == 2:   
                # Player chooses to block
                # If player wins the block game, deal damage to enemy
                # If player loses the block game, no effect
                if enemy1.blockGame():
                    enemy1.health -= 30
                    print("The enemy has been hit for 30 damage and is now at", enemy1.health)
                    blockGameWinner = True
                else:
                    blockGameWinner = False
                answer2 = True 
            elif answer == 3:
                # Player chooses to use an item (not implemented)
                answer2 = True
            elif answer == 4:
                # Player chooses to run (not successful)
                print('You failed to run and lost your turn.')
                answer2 = True
            else:   
                print('This is not an option')

        # Check if enemy is defeated
        if enemy1.health <= 0:
            answer1 = True
            break

        # Enemy's turn
        if player.specialMove(enemy1.health, specialAttack) == 1:
            player.health = enemy1.enemyAttack(player.health)
        elif blockGameWinner == False:
            player.health = enemy1.enemyAttack(player.health)

        # Check if player is defeated
        if player.health <= 0:
            quit()
            Lost = True
            answer1 = True
        else:
            answer2 = False

    # Transition to next area
    print("Alright looks light you are moving on from the first boss.")
    print("You will now leave the starter tower.")

    # Location selection loop
    while choseLocation1 == False:
        location1 = int(input("If you would like to enter the beach click 1 or the next boss's room click 2?"))
        if location1 == 1:
            # Player chooses to enter the beach
            print("Good choice. You will now enter the beach.")
            room1 = laca.room("Beach room 1", 150, 7, 7, 4)
            room1.roomGen(player, sword, enemy1) 
            quit()
            choseLocation1 = True
        elif location1 == 2:
            # Player chooses to skip to the next boss
            print("Ok. Sending you to the boss room")
            choseLocation1 = True
        else:
            print("That is not an option.")   
from random import randint
import numpy as np
import items as ight

# The Player class represents a player in the game with certain attributes and methods.
class player:
    # The __init__ method initializes the player with certain attributes like class, ability, speed, damage, weapon, health, and location.
    def __init__(self, Class, ability, speed, damage, weapon, health, location, x, y, px, py):
        self.Class = Class
        self.ability = ability
        self.speed = speed
        self.damage = damage
        self.weapon = weapon
        self.health = health
        self.location = location
        self.x = x
        self.y = y
        self.px = px
        self.py = py

    # The __str__ method provides a string representation of the player object.
    def __str__(self):
        return f"Class: {self.Class}, Ability: {self.ability}, Speed: {self.speed}, Damage: {self.damage}, Weapon: {self.weapon}, Health: {self.health}, Location: {self.location}"
    
    # The specialMove method defines the special moves that can be performed by the player based on their class.
    def specialMove(self, enemyHealth, specialAttack):
        fireDamage = 5

        if self.Class == "Rogue":
            print("All righty, back to your turn")
            return 0
        elif self.Class == "Mage":
            print("The enemy was hit for", fireDamage, "because of your fire special move")
            enemyHealth -= fireDamage
            return 1

    ## The attackMath method calculates the damage dealt to the enemy based on the player's class, 
    # their speed, and whether a special attack or double attack was made.
    def attackMath(self, enemy1Health, specialAttack):
    #Double attack = Speed x 2
    #Special attack = 35 without double attack happening
    #Special attack = 20 with double attack happening
    #sPA = Special Attack
    #sPAWD = Special Attack with Double Attack
        startDamage = self.weapon.damage + self.damage
        doubleAttackAns = randint(1, 100)
        specialAttackAns = randint(1, 100)
        doubleAttackPerc = self.speed*2
        sPAWD = 20
        sPA = 35
        if doubleAttackAns <= doubleAttackPerc:
            #Double attack happens
            if specialAttackAns <= sPAWD:
                #Double attack + special attack happens
                if self.Class == "Berserk":
                    damage = startDamage*4
                    print("You went Berserk and hit the enemy for 2x damage with a double attack too. This hit him for", damage)
                    enemy1Health -= damage
                elif self.Class == "Mage":
                    damage = startDamage*2
                    print("You used your set fire ability and double attack in the same move. This hit him for", damage, "and now he will take 5 damage every turn because you set him on fire")
                    enemy1Health -= damage
                    specialAttack = True
                elif self.Class == "Rogue":
                    damage = startDamage*3
                    print("You used your triple attack and your special dodge move in the same turn. This hit him for", damage, "you will now dodge his next turn")
                    enemy1Health -= damage
                    specialAttack = True
                elif self.Class == "Archer":
                    damage = startDamage*3
                    print("You used your double attack and special move to freely full charge back. This hit the enemy for", damage)
                    enemy1Health -= damage

            else:
                #Just double attack happens
                if self.Class == "Rogue":
                    damage = startDamage*3
                    print("You hit the enemy with a triple attack for", damage, 'health')
                    enemy1Health -= damage

                else:
                    damage = startDamage*2
                    print("You hit the enemy with a double attack for", damage, 'health')
                    enemy1Health -= damage


        else:
            #No double attack
            if specialAttackAns <= sPA:
                #Special attack happens
                if self.Class == "Berserk":
                    damage = startDamage*2
                    print("You went Berserk and hit the enemy for 2x damage. This hit him for", damage, "and you will also hit him for 2x damage for the next 2 turns")
                    enemy1Health -= damage
                    specialAttack1 = True
                    bAttack = 0
                elif self.Class == "Mage":
                    damage = startDamage
                    print("You used your set fire ability. This hit him for", damage, "and now he will take 5 damage every turn because you set him on fire")
                    enemy1Health -= damage
                    specialAttack = True
                elif self.Class == "Rogue":
                    damage = startDamage
                    print("You used your special dodge move. This hit him for", damage, "you will now dodge his next turn")
                    enemy1Health -= damage
                    specialAttack = True
                elif self.Class == "Archer":
                    damage = startDamage*1.5
                    print("You used your special move to freely full charge back. This hit the enemy for", damage)
                    enemy1Health -= damage

            else:
                #Normal attack happens
                damage = startDamage
                print("You hit the enemy for", damage, 'health')
                enemy1Health -= damage

        if enemy1Health <= 0:
            print("The enemy is at 0 health.\nNice job you defeated the boss")
            enemy1Health = 0
        else:
            print("The enemy is at", enemy1Health, "health")

        if specialAttack:
            self.specialMove(enemy1Health, specialAttack)

        return enemy1Health
    
    # Define a method to visualize the player
    def playerLook(self):
        return " o "


    # handles the player's action of picking up an item
    def pickUp(self, generateItems, allItems):
        chose = False
        correct = False
        weaponMain = False
        weaponIn = False
        food = False
        armorMain = False
        armorIn = False
        foodMain = False
        foodIn = False
        if generateItems == False:
            return None
        
        else:
            while correct == False:
                for x in range(len(allItems)):
                    if generateItems == allItems[x]:
                        pickedItem = allItems[x]
                        correct = True

            print("You picked up", pickedItem.name)
            while chose == False:
                if not pickedItem.damage == 0:
                    #Has to be weapon
                    ans = int(input("Would you like to add", pickedItem.name, "to be your main weapon. \nIf so press 1 and if not press 2\n"))
                    if input == 1:
                        print("The weapon you obtained has been made your main weapon")
                        weaponMain = True
                        chose = True
                    elif input == 2:
                        print("The weapon you obtained has been added to your inventory")
                        weaponIn = True
                        chose = True
                    else:
                        print("This is not an option")
                
                elif not pickedItem.protection == 0:
                    #Has to be an armor piece
                    ans = int(input("Would you like to add", pickedItem.name, "to be your main armor piece in the given spot. \nIf so press 1 and if not press 2\n"))
                    if input == 1:
                        print("The armor piece you obtained has been made your main armor piece in the named area")
                        armorMain = True
                        chose = True
                    elif input == 2:
                        print("The armor piece you obtained has been added to your inventory")
                        armorIn = True
                        chose = True
                    else:
                        print("This is not an option")

                else:
                    #Has to be food
                    ans = int(input("Would you like to add", pickedItem.name, "to be your a food in your hotbar. \nIf so press 1 and if not press 2\n"))
                    if input == 1:
                        print("The food you obtained has been put in your hotbar")
                        foodMain = True
                        chose = True
                    elif input == 2:
                        print("The armor piece you obtained has been added to your inventory")
                        foodIn = True
                        chose = True
                    else:
                        print("This is not an option")

            
            if weaponMain:
                #Make weapon main
                print('This will make the weapon the main weapon')
                return 0
            elif weaponIn:
                #Put weapon in inventory
                print('This will put the weapon in the inventory')
                return 1
            elif armorMain:
                #Make armor main
                print('This will make the armor the main armor piece for that slot')
                return 2
            elif armorIn:
                #Put armor in inventory
                print('This will put the armor in the inventory')
                return 3
            elif foodIn:
                #Put food in inventory
                print('This will put the food in the inventory')
                return 4
            elif foodMain:
                #Put food in hotbar
                print('This will put the food your hotbar')
                return 5

    # sorts the items in the player's inventory
    def sortItem(self, items, allItems, generateItems, inventory):
        space = False
        correct = False
        inventoryCheck = False
        if generateItems == False:
            return None
        
        else:
            while correct == False:
                for x in range(len(allItems)):
                    if generateItems == allItems[x]:
                        pickedItem = allItems[x]
                        correct = True

        inventoryPart = self.pickUp(generateItems, allItems)

        if inventoryPart == 1:
            #Weapon in inventory
            #Need to go from 1,0 to 2,10
            y = 2
            x = 22
            inventoryCheck = True

        elif inventoryPart == 3:
            #Armor in inventory
            #Need to go from 3,0 to 5,10
            y = 3
            x = 33
            inventoryCheck = True
            
        elif inventoryPart == 4:
            #Food in inventory
            #Need to go from 6,0 to 7,10
            y = 2
            x = 22
            inventoryCheck = True

        elif inventoryPart == 0: 
            #Weapon in hotbar
            #Need to check main weapon
            #Weapon goes into 0,0
            if inventory[0][0] == '_ ':
                return 0, 0

        elif inventoryPart == 2:
            #Armor in hotbar
            #Need to check main armor in given spot
            #Check which armor piece
            #Helmet = 0, 1 Chest = 0,2 Leg = 0,3 Boot = 0,4
            if pickedItem.function == "Helmet":
                if inventory[0][1] == '_ ':
                    return 0, 1

            elif pickedItem.function == "Chestplate":
                if inventory[0][2] == '_ ':
                    return 0, 2

            elif pickedItem.function == "Leggings":
                if inventory[0][3] == '_ ':
                    return 0, 3

            elif pickedItem.function == "Boots":
                if inventory[0][4] == '_ ':
                    return 0, 4
            

        elif inventoryPart == 5:
            #Food in hotbar
            #Need to check main food slots
            #Food goes from 0,5 to 0,9
            i = 5
            y = 0
            for x in range(i):
                y = x
                x = x + 5
                if inventory[0][x] == '_ ':
                    return 0, x
                x = y + 1

            inventoryCheck = True

        else:
            return None
        
        if inventoryCheck:
            for i in range(y):
                for j in range(x):
                    if(inventory[y][x] == "_ "):
                        #Spot is open
                        return i, j
        
        return 1
                    
    # handles the player's inventory, including displaying it and adding items to it.
    def inventory(self, item, allItems, generateItems):
        #Need to make a 2d array
        print("Row 1 is for your hotbar")
        print("Rows 2 and 3 are for weapons")
        print("Rows 4, 5, and 6 are for armor")
        print("Rows 7 and 8 are for food\n")
        print("[Inventory]")
        inventory = [[' ']*10 for i in range(8)]
        # if self.sortItem(item, allItems, generateItems, inventory) == 1:
        #     #No spot available
        # else:
        thing = self.sortItem(item, allItems, generateItems, inventory)
        print(thing)
        inventory[1][2] = item
        for row in inventory:
            for item in row:
                if isinstance(item, str):
                    print(item, end='_ ')
                else:
                    print(item.rp, end=' ')  # or whatever attribute you want to display
            print()

        #print(inventory[1][1].protection)
        return inventory

# Example usage of the player class
self1 = player("Berserk", "GO BERSERK", 5, 30, "thing", 160, None, 0, 0, 0, 0)
item = ight.item("Gold Helmet", "Protection", 1, 100, 0, 40, 0, False, "GH")
# thing = self1.sortItem(item, allItems, generateItems, inventory)
# print(thing)
# self1.inventory(item)

        
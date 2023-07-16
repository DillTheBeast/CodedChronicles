import locations as laca
import player as playa
import enemy1 as bigboypants
import weapons as wepawn
import numpy as np
import items as ight
from random import randint

def generateItems(room, player, weapons, items, enemyLocation, roomPic, enemy, allItems):
    for i in range(len(enemyLocation)):
        for j in range(2):
            #Range 2 for each coordinate
            if j == 1:
                #x coordinate
                enemyX = enemyLocation[j]
            else:
                #y coordinate
                enemyY = enemyLocation[j]
        if roomPic[enemyX][enemyY] == enemy.enemyLook():
            #Enemy still there
            break
        else:
            #Enemy not there anymore
            roomPic[enemyX][enemyY] = "i "
            sectionAns = randint(1, 9)
            pointAns = randint(1, 2)
            if sectionAns == 1:
                #Go to swords
                if pointAns == 1:
                    #Find which thing in the section
                    return allItems[0]

                elif pointAns == 2:
                    return allItems[1]

            elif sectionAns == 2:
                #Go to staffs
                if pointAns == 1:
                    #Find which thing in the section
                    return allItems[2]

                elif pointAns == 2:
                    return allItems[3]

            elif sectionAns == 3:
                #Go to daggers
                if pointAns == 1:
                    #Find which thing in the section
                    return allItems[4]
                
                elif pointAns == 2:
                    return allItems[5]

            elif sectionAns == 4:
                #Go to bows
                if pointAns == 1:
                    #Find which thing in the section
                    return allItems[6]

                elif pointAns == 2:
                    return allItems[7]

            elif sectionAns == 5:
                #Go to food
                if pointAns == 1:
                    #Find which thing in the section
                    return allItems[8]

                elif pointAns == 2:
                    return allItems[9]

            elif sectionAns == 6:
                #Go to helmets
                if pointAns == 1:
                    #Find which thing in the section
                    return allItems[10]

                elif pointAns == 2:
                    return allItems[11]

            elif sectionAns == 7:
                #Go to chestplates
                if pointAns == 1:
                    #Find which thing in the section
                    return allItems[12]

                elif pointAns == 2:
                    return allItems[13]

            elif sectionAns == 8:
                #Go to Leggings
                if pointAns == 1:
                    #Find which thing in the section
                    return allItems[14]

                elif pointAns == 2:
                    return allItems[15]

            else:
                #Go to boots
                if pointAns == 1:
                    #Find which thing in the section
                    return allItems[16]
                
                elif pointAns == 2:
                    return allItems[17]
    return False

        
def itemList(items):
    allItems = []
    #Swords
    sword1 = ight.item("Sword1", "weapon", 1, 100, 50, 0, 0, False, "SW1")
    sword2 = ight.item("Sword2", "weapon", 1, 100, 100, 0, 0, False, "SW2")
    sword3 = ight.item("Sword3", "weapon", 1, 100, 200, 0, 0, True, "Sw3")
    #Staffs
    staff1 = ight.item("Staff1", "weapon", 1, 100, 40, 0, 0, False, "ST1")
    staff2 = ight.item("Staff2", "weapon", 1, 100, 80, 0, 0, False, "ST2")
    staff3 = ight.item("Staff3", "weapon", 1, 100, 160, 0, 0, True, "ST3")
    #Daggers
    dagger1 = ight.item("Dagger1", "weapon", 1, 100, 20, 0, 0, False, "D1 ")
    dagger2 = ight.item("Dagger2", "weapon", 1, 100, 40, 0, 0, False, "D2 ")
    dagger3 = ight.item("Dagger3", "weapon", 1, 100, 80, 0, 0, True, "D3 ")
    #Bows
    bow1 = ight.item("Bow1", "weapon", 1, 100, 30, 0, 0, False, "B1 ")
    bow2 = ight.item("Bow2", "weapon", 1, 100, 60, 0, 0, False, "B2 ")
    bow3 = ight.item("Bow3", "weapon", 1, 100, 90, 0, 0, True, "B3 ")
    #Heals
    food = ight.item("Raw Food", "Heal", 5, 1, 0, 0, 20, False, " F ")
    potion = ight.item("Potion", "Heal", 5, 1, 0, 0, 50, False, " P ")
    cookedFood = ight.item("Cooked Food", "Heal", 5, 1, 0, 0, 80, True, "CF ")
    #Helmets
    ironHelm = ight.item("Iron Helmet", "Protection", 1, 100, 0, 20, 0, False, "IH ")
    goldHelm = ight.item("Gold Helmet", "Protection", 1, 100, 0, 40, 0, False, "GH ")
    diamondHelm = ight.item("Diamond Helmet", "Protection", 1, 100, 0, 80, 0, True, "DH ")
    #Chestplates
    ironChest = ight.item("Iron Chestplate", "Protection", 1, 100, 0, 40, 0, False, "IC ")
    goldChest = ight.item("Gold Chestplate", "Protection", 1, 100, 0, 80, 0, False, "GC ")
    diamondChest = ight.item("Diamond Chestplate", "Protection", 1, 100, 0, 160, 0, True, "DC ")
    #Leggings
    ironLeg = ight.item("Iron Leggings", "Protection", 1, 100, 0, 30, 0, False, "IL ")
    goldLeg = ight.item("Gold Leggings", "Protection", 1, 100, 0, 60, 0, False, "GL ")
    diamondLeg = ight.item("Diamond Leggings", "Protection", 1, 100, 0, 120, 0, True, "DL ")
    #Boots
    ironBoots = ight.item("Iron Boots", "Protection", 1, 100, 0, 10, 0, False, "IB ")
    goldBoots = ight.item("Gold Boots", "Protection", 1, 100, 0, 20, 0, False, "GB ")
    diamondBoots = ight.item("Diamond Boots", "Protection", 1, 100, 0, 40, 0, True, "DB ")

    allItems.append(sword1, sword2)
    allItems.append(staff1, staff2)
    allItems.append(dagger1, dagger2)
    allItems.append(bow1, bow2)
    allItems.append(food, potion)
    allItems.append(ironHelm, goldHelm)
    allItems.append(ironChest, goldChest)
    allItems.append(ironLeg, goldLeg)
    allItems.append(ironBoots, goldBoots)
    allItems.append(sword3, staff3, dagger3, bow3, cookedFood, diamondHelm, diamondChest, diamondLeg, diamondBoots)

    return allItems

sword = wepawn.weapon("Starter Sword", "Sword", 7, 100, None, False, "Starter", "Start", False)
player = playa.player("Berserk", "GO BERSERK", 5, 30, sword, 160, None)
items = "as"
arr = []
room1 = laca.room("beach", 90, 7, 7, 4, arr)
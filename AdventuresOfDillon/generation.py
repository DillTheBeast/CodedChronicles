import locations as laca
import player as playa
import enemy1 as bigboypants
import weapons as wepawn
import numpy as np
import items as ight

def generateItems(room, player, weapons, items, enemyLocation, roomPic, enemy):
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

        
def itemList(items):
    #Swords
    sword1 = ight.item("Sword1", "weapon", 1, 100)
    sword2 = ight.item("Sword2", "weapon", 1, 100)
    sword3 = ight.item("Sword3", "weapon", 1, 100)
    #Staffs
    staff1 = ight.item("Staff1", "weapon", 1, 100)
    staff2 = ight.item("Staff2", "weapon", 1, 100)
    staff3 = ight.item("Staff3", "weapon", 1, 100)
    #Daggers
    dagger1 = ight.item("Dagger1", "weapon", 1, 100)
    dagger2 = ight.item("Dagger2", "weapon", 1, 100)
    dagger3 = ight.item("Dagger3", "weapon", 1, 100)
    #Bows
    bow1 = ight.item("Bow1", "weapon", 1, 100)
    bow2 = ight.item("Bow2", "weapon", 1, 100)
    bow3 = ight.item("Bow3", "weapon", 1, 100)
    #Heals
    food = ight.item("Food", "Heal", 5, 1)
    potion = ight.item("Potion", "Heal", 5, 1)
    cookedFood = ight.item("Cooked Food", "Heal", 5, 1)
    #Helmets
    ironHelm = ight.item("Iron Helmet", "Protection", 1, 100)
    goldHelm = ight.item("Gold Helmet", "Protection", 1, 100)
    diamondHelm = ight.item("Diamond Helmet", "Protection", 1, 100)
    #Chestplates
    ironChest = ight.item("Iron Chestplate", "Protection", 1, 100)
    goldChest = ight.item("Gold Chestplate", "Protection", 1, 100)
    diamondChest = ight.item("Diamond Chestplate", "Protection", 1, 100)
    #Leggings
    ironLeg = ight.item("Iron Leggings", "Protection", 1, 100)
    goldLeg = ight.item("Gold Leggings", "Protection", 1, 100)
    diamondLeg = ight.item("Diamond Leggings", "Protection", 1, 100)
    #Boots
    ironBoots = ight.item("Iron Boots", "Protection", 1, 100)
    goldBoots = ight.item("Gold Boots", "Protection", 1, 100)
    diamondBoots = ight.item("Diamond Boots", "Protection", 1, 100)



sword = wepawn.weapon("Starter Sword", "Sword", 7, 100, None, False, "Starter", "Start", False)
player = playa.player("Berserk", "GO BERSERK", 5, 30, sword, 160, None)
items = "as"
arr = []
room1 = laca.room("beach", 90, 7, 7, 4, arr)
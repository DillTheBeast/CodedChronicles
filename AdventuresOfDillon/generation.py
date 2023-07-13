import locations as laca
import player as playa
import enemy1 as bigboypants
import weapons as wepawn
import numpy as np

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

        





sword = wepawn.weapon("Starter Sword", "Sword", 7, 100, None, False, "Starter", "Start", False)
player = playa.player("Berserk", "GO BERSERK", 5, 30, sword, 160, None)
items = "as"
arr = []
room1 = laca.room("beach", 90, 7, 7, 4, arr)
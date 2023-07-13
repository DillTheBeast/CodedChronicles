import locations as laca
import player as playa
import enemy1 as bigboypants
import weapons as wepawn
import numpy as np

def findLocations(room, player, weapons, items):
    room.roomGen(player, weapons, items)
    enemyLocation = [np.array([[x,y]])]

    for y in range(room.height):
        for x in range(room.length):
            if(room.roomPic[x][y] == "x "):
                enemyLocation.append(int(room.roomPic[x][y]))

    print(enemyLocation)
    return enemyLocation


#def generateItems(room, player, weapons, items, enemyLocation):
        # for i in range(enemyLocation):
        #      for j in range(enemyLocation):

        # for y in range(room.height):
        #     for x in range(room.length):
        #         if(room.roomPic[y][x] == "x "):
        #             enemyLocation.append(room.roomPic[y][x])
sword = wepawn.weapon("Starter Sword", "Sword", 7, 100, None, False, "Starter", "Start", False)
player = playa.player("Berserk", "GO BERSERK", 5, 30, sword, 160, None)
items = "as"
arr = []
room1 = laca.room("beach", 90, 7, 7, 4, arr)
findLocations(room1, player, sword, items)
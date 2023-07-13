from random import randint
import numpy as np

class location:
    def __init__(location, name, difficulty, itemSpawnRate):
        location.name = name
        location.difficulty = difficulty
        location.itemSpawnRate = itemSpawnRate


    def __str__(location):
        return f"Name: {location.name}, Difficulty: {location.difficulty}, Item Spawn Rate: {location.itemSpawnRate}"
    

    # def itemSpawnRateCalc(location, items):
    #     spawnNum = randint(1, len(items))

    # def enemySpawnRateCalc(location, enemy):


class room:
    def __init__(room, name, temp, height, length, enemyCount):
        room.name = name
        room.temp = temp
        room.height = height
        room.length = length
        room.enemyCount = enemyCount



    def __str__(room):
        return f"Name: {room.name}, Temperature: {room.temp}, Height: {room.height}, Length: {room.length}, Enemy Counter: {room.enemyCount}"
    

    def roomGen(room):
        print("The o will represent you and the x represents the enemy. Move around to find the hidden items")
        # roomPic = np.array([[], []])
        # enemies = room.enemyCount
        # enemyList = []

        # for y in range(room.height):
        #     for x in range(room.length): 
        #         roomPic[x][y] = "_ "                                   

        # for enemy in range(enemies):
        #     enemyX = randint(0, room.length-1)
        #     enemyY = randint(0, room.height-1)

        # roomPic[1][1] = "x "
        # print(roomPic[1][3])
        # print(roomPic)

        # for y in range(room.height):
        #     for x in range(room.length):
        #         #print(y, end = '')
        #         #print(x, end = '')
        #         print(roomPic[x][y], end = '')
        #     print(' ')

        roomPic = np.full((room.height, room.length), "_ ")

        for enemy in range(room.enemyCount):
            enemyX = randint(0, room.length-1)
            enemyY = randint(0, room.height-1)
            roomPic[enemyY, enemyX] = "x "

        playerX = randint(0, room.length-1)
        playerY = randint(0, room.height-1)
        roomPic[playerY, playerX] = "o "

        print('\n'.join([' '.join(row) for row in roomPic]))

room1 = room("Beach1", 90, 7, 7, 4)

room1.roomGen()
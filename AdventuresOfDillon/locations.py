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
    def __init__(room, name, temp, height, length, enemyCount, roomPic):
        room.name = name
        room.temp = temp
        room.height = height
        room.length = length
        room.enemyCount = enemyCount
        room.roomPic = roomPic



    def __str__(room):
        return f"Name: {room.name}, Temperature: {room.temp}, Height: {room.height}, Length: {room.length}, Enemy Counter: {room.enemyCount}"
    

    def roomGen(room, player, weapons, items):
        print("The o will represent you and the x represents the enemy. Move around to find the hidden items")

        room.roomPic = np.full((room.height, room.length), "_ ")

        for enemy in range(room.enemyCount):
            enemyX = randint(0, room.length-1)
            enemyY = randint(0, room.height-1)
            room.roomPic[enemyY, enemyX] = "x "

        room.roomPic[0, 0] = player.playerLook()

        print('\n'.join([' '.join(row) for row in room.roomPic]))

        return room.roomPic


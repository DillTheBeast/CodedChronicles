from random import randint

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
    def __init__(room, name, temp, height, length):
        room.name = name
        room.temp = temp
        room.height = height
        room.length = length



    def __str__(room):
        return f"Name: {room.name}, Temperature: {room.temp}, Height: {room.height}, Length: {room.length}"
    

    def roomGen():
        rows, cols = (5, 5)
        print("The o will represent you and the x represents the enemy. Move around to find the hidden items")
        room = [['_'] * cols]*rows
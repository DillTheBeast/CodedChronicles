# Import necessary libraries and modules
from random import randint
import numpy as np
import player as playa
import enemy1 as bigboypants
import weapons as wepawn
import items as ight

# Define the location class
class location:
    # Initialize the location with various attributes
    def __init__(location, name, difficulty, itemSpawnRate):
        location.name = name  # Name of the location
        location.difficulty = difficulty  # Difficulty level of the location
        location.itemSpawnRate = itemSpawnRate  # Item spawn rate at the location

    # Method to print out the location's details in a friendly format
    def __str__(location):
        return f"Name: {location.name}, Difficulty: {location.difficulty}, Item Spawn Rate: {location.itemSpawnRate}"

# Define the room class
class room:
    # Initialize the room with various attributes
    def __init__(room, name, temp, height, length, enemyCount):
        room.name = name  # Name of the room
        room.temp = temp  # Temperature of the room
        room.height = height  # Height of the room (rows in the grid)
        room.length = length  # Length of the room (columns in the grid)
        room.enemyCount = enemyCount  # Number of enemies in the room
        room.roomPic = roomPic  # 2D array representing the room

    # Method to print out the room's details in a friendly format
    def __str__(room):
        return f"Name: {room.name}, Temperature: {room.temp}, Height: {room.height}, Length: {room.length}, Enemy Counter: {room.enemyCount}"

    # Method to generate the room's layout
    def roomGen(room, player, weapons, items, enemy):
        print("The o will represent you and the x represents the enemy. Move around to find the hidden items")

        # Create an array for the room layout
        room.roomPic = [[' ']*room.length for i in range(room.height)]

        # Place the player in the room
        room.roomPic[0][0] = player.playerLook()

        # Generate enemies in the room
        room.enemyGen(enemy, room.roomPic)

        # Print the room layout
        for row in room.roomPic:
            for item in row:
                if isinstance(item, str):
                    print(item, end=' _ ')
                else:
                    print(item.rp, end=' ')  # or whatever attribute you want to display
            print()

        return room.roomPic

    # Method to generate enemies in the room
    def enemyGen(room, enemy, roomPic):
        enemyLocation = []  # List to store the locations of the enemies
        found = False  # Flag to indicate if a valid location for an enemy has been found

        # Generate enemies
        for enemies in range(room.enemyCount):
            found = False
            while found == False:
                # Randomly select a location for the enemy
                enemyX = randint(0, room.length-2)
                enemyY = randint(0, room.height-1)
                print(enemyX)
                print(enemyY)
                # Ensure the enemy is not placed on the player's location
                if not enemyX == 0 and not enemyY == 0:
                    room.roomPic[enemyX][enemyY] = enemy.enemyLook()
                    found = True
                # Add the enemy's location to the list
                enemyLocation.append(enemyX)
                enemyLocation.append(enemyY)
        return enemyLocation
    

# self1 = playa.player("Berserk", "GO BERSERK", 5, 30, "thing", 160, None)
# item = ight.item("Gold Helmet", "Protection", 1, 100, 0, 40, 0, False, "GH")
# sword = wepawn.weapon("Starter Sword", "Sword", 7, 100, None, False, "Starter", "Start", False)
# enemy1 = bigboypants.enemy1("Eldredge Dragon", 10, 300)
# room1 = room("Plain", 90, 7, 8, 4, room.roomGen)
# room.roomGen(room1, self1, sword, item, enemy1,)
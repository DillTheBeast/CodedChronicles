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
        room.roomPic = [[' ']*room.length for i in range(room.height)]  # 2D array representing the room

    # Method to print out the room's details in a friendly format
    def __str__(room):
        return f"Name: {room.name}, Temperature: {room.temp}, Height: {room.height}, Length: {room.length}, Enemy Counter: {room.enemyCount}"

    # Method to generate the room's layout
    def roomGen(room, player, weapons, enemy):
        print("The o will represent you and the x represents the enemy. Move around to find the hidden items")

        # Create an array for the room layout
        room.roomPic = [[' ']*room.length for i in range(room.height)]

        # Place the player in the room
        room.roomPic[0][0] = player.playerLook()
        playerLocX = 0
        playerLocY = 0

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
                # Ensure the enemy is not placed on the player's location
                if not enemyX == 0 and not enemyY == 0:
                    room.roomPic[enemyX][enemyY] = enemy.enemyLook()
                    found = True
                # Add the enemy's location to the list
                enemyLocation.append(enemyX)
                enemyLocation.append(enemyY)
        return enemyLocation
    
    #Makes the player move accross the room/board
    def playerMove(room, player, playerLocX, playerLocY):
        chose = False
        print('x:', playerLocX)
        print('y:', playerLocY)
        while not chose:
            direction = input('Which way would you like to move.\nPress w to move up, d to move right, s to move down, and a to move left ')

            if direction == 'w':
                if not playerLocY - 1 == -1:
                    previousLocY = playerLocY
                    previousLocX = playerLocX
                    playerLocY -= 1
                    chose = True
                else:
                    print("You can't move in this direction")

            elif direction == 's':
                if not playerLocY == 8:
                    previousLocY = playerLocY
                    previousLocX = playerLocX
                    playerLocY += 1
                    chose = True
                else:
                    print("You can't move in this direction")

            elif direction == 'a':
                if not playerLocX - 1 == -1:
                    previousLocY = playerLocY
                    previousLocX = playerLocX
                    playerLocX -= 1
                    chose = True
                else:
                    print("You can't move in this direction")

            elif direction == 'd':
                if not playerLocX == 7:
                    previousLocY = playerLocY
                    previousLocX = playerLocX
                    playerLocY += 1
                    chose = True
                else:
                    print("You can't move in this direction")

            else:
                print("You can't chose that option")

        #Player is able to and has moved in that direction
        print('x:', playerLocX)
        print('y:', playerLocY)
        return playerLocX, playerLocY, previousLocX, previousLocY
    
    def boardMove(room, player, playerLocX, playerLocY, previousLocX, previousLocY):
        print('x:', playerLocX)
        print('y:', playerLocY)
        room.roomPic[previousLocX][previousLocY] = ' _ '
        room.roomPic[playerLocX][playerLocY] = player.playerLook()
        for row in room.roomPic:
            for item in row:
                if isinstance(item, str):
                    print(item, end=' _ ')
                else:
                    print(item.rp, end=' ')  # or whatever attribute you want to display
            print()
    
self1 = playa.player("Berserk", "GO BERSERK", 5, 30, "thing", 160, None)
# item = ight.item("Gold Helmet", "Protection", 1, 100, 0, 40, 0, False, "GH")
# sword = wepawn.weapon("Starter Sword", "Sword", 7, 100, None, False, "Starter", "Start", False)
# enemy1 = bigboypants.enemy1("Eldredge Dragon", 10, 300)
room1 = room("Plain", 90, 7, 8, 4)
# room.roomGen(room1, self1, sword, item, enemy1,)
x = 0
y = 0
while True:
    print(x)
    print(y)
    room.boardMove(room1, self1, room.playerMove(room1, self1, x, y))
    print(x)
    print(y)
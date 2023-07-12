class location:
    def __init__(location, name, difficulty, itemSpawnRate):
        location.name = name
        location.difficulty = difficulty
        location.itemSpawnRate = itemSpawnRate


    def __str__(location):
        return f"Name: {location.name}, Difficulty: {location.difficulty}, Item Spawn Rate: {location.itemSpawnRate}"
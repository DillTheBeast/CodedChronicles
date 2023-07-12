class item:
    def __init__(item, name, function, amount, durability):
        item.name = name
        item.function = function
        item.amount = amount
        item.durability = durability


    def __str__(item):
        return f"Name: {item.name}, Function: {item.function}, Amount: {item.amount}, Durability: {item.durability}"
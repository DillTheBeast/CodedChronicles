class item:
    def __init__(item, name, function, amount, durability, damage, protection, health, isHidden):
        item.name = name
        item.function = function
        item.amount = amount
        item.durability = durability
        item.damage = damage
        item.protection = protection
        item.health = health
        item.isHidden = isHidden


    def __str__(item):
        return f"Name: {item.name}, Function: {item.function}, Amount: {item.amount}, Durability: {item.durability}, Damage: {item.damage}, Protection: {item.protection}, Healing Health: {item.health}"
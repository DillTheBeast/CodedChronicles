# Define the item class
class item:
    def __init__(item, name, function, amount, durability, damage, protection, health, isHidden, rp):
        item.name = name  # Name of the item
        item.function = function  # Functionality of the item (e.g., weapon, armor, etc.)
        item.amount = amount  # The amount of this item
        item.durability = durability  # How durable the item is
        item.damage = damage  # How much damage this item can cause (if it's a weapon)
        item.protection = protection  # How much protection this item provides (if it's an armor)
        item.health = health  # How much health this item can restore (if it's food)
        item.isHidden = isHidden  # Whether this item is hidden or not
        item.rp = rp  # The representation of the item for printing


    # Method to print out the item's details in a friendly format
    def __str__(item):
        return f"Name: {item.name}, Function: {item.function}, Amount: {item.amount}, Durability: {item.durability}, Damage: {item.damage}, Protection: {item.protection}, Healing Health: {item.health}"
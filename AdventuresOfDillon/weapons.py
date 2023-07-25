# Define the weapon class
class weapon:
    # Initialize the weapon with various attributes
    def __init__(weapon, name, type, damage, durability, enchantments, isEnchantable, rarity, location, isHidden):
        weapon.name = name  # Name of the weapon
        weapon.type = type  # Type of the weapon (e.g., sword, bow, etc.)
        weapon.damage = damage  # Damage inflicted by the weapon
        weapon.durability = durability  # Durability of the weapon
        weapon.enchantments = enchantments  # Any enchantments on the weapon
        weapon.isEnchantable = isEnchantable  # Whether the weapon can be enchanted
        weapon.rarity = rarity  # The rarity of the weapon
        weapon.location = location  # Where the weapon was found
        weapon.isHidden = isHidden  # Whether the weapon is hidden or not

    # Method to print out the weapon's details in a friendly format
    def __str__(weapon):
        return f"Name: {weapon.name}, Type: {weapon.type}, Damage: {weapon.damage}, Durability: {weapon.durability}, Enchantments: {weapon.enchantments}, Rarity: {weapon.rarity}, Location: {weapon.location}, isHidden: {weapon.isHidden}"
    
    # Method to check the location of the weapon
    def locationChecker(weapon):
        # Possible Locations = Dungeon, Forest, Beach, Ocean, BossBuilding
        if weapon.location == "Dungeon":
            return 3
        elif weapon.location == "Forest":
            return 2
        elif weapon.location == "Beach":
            return 1
        elif weapon.location == "Ocean":
            return 4
        elif weapon.location == "BossBuilding":
            return 5
        
    # Method to calculate the rarity of the weapon based on player's luck and whether the weapon is hidden or not
    def rarityCalc(weapon, playerLuck, isHidden):
        luckNum = playerLuck/10 
        placeNum = weapon.locationChecker()
        if isHidden:
            endNum = luckNum + placeNum + 1
        else:
            endNum = luckNum + placeNum
        if endNum < 3:
            # Common
            return "Common"
        elif endNum < 6:
            # Uncommon
            return "Uncommon"
        elif endNum < 9:
            # Rare
            return "Rare"
        elif endNum < 12:
            # Epic
            return "Epic"
        else:
            # Legendary
            return "Legendary"

    # Method to check if a weapon can be enchanted
    # def enchantableCheck(weapon, luck, type):
    #     if luck >= 20:
    #         return True
    #     else:
    #         return False

    # Method to handle enchanting a weapon
    def enchants(weapon, luck):
        if weapon.enchantableCheck:
            # Weapon can be enchanted
            print("Test")
        else:
            print("You need luck 20 before you can enchant")
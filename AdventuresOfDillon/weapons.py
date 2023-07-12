class weapon:
    #Need functions to make rarity of sword depending on luck + where found
    
    def __init__(weapon, name, type, damage, durability, enchantments, isEnchantable, rarity, location, isHidden):
        weapon.name = name
        weapon.type = type
        weapon.damage = damage
        weapon.durability = durability
        weapon.enchantments = enchantments
        weapon.isEnchantable = isEnchantable
        weapon.rarity = rarity
        weapon.location = location
        weapon.isHidden = isHidden


    def __str__(weapon):
        return f"Name: {weapon.name}, Type: {weapon.type}, Damage: {weapon.damage}, Durability: {weapon.durability}, Enchantments: {weapon.enchantments}, Rarity: {weapon.rarity}, Location: {weapon.location}, isHidden: {weapon.isHidden}"
    
    def locationChecker(weapon):
        #Possible Locations = Dungeon, Forest, Beach, Ocean, BossBuilding
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
        
    def rarityCalc(weapon, playerLuck):
        luckNum = playerLuck/5
        


    # def enchantableCheck(weapon, luck, type):
    #     if luck >= 20:
    #         return True
    #     else:
    #         return False

    def enchants(weapon, luck):
        if weapon.enchantableCheck:
            #Means that we can enchant
            print("Test")
        else:
            print("You need luck 20 before you can enchant")
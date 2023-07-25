from random import randint
import math as m

# Define the enemy class
class enemy1:
    # Enemy class constructor
    def __init__(enemy, name, damage, health):
        enemy.name = name
        enemy.damage = damage
        enemy.health = health

    # Define string representation of enemy
    def __str__(enemy):
        return f"Name: {enemy.name}, Damage: {enemy.damage}, Health: {enemy.health}"
    
    # Define a blocking game for the enemy
    def blockGame(enemy):
        # Randomly select a number and get player's guess
        # The player or enemy closer to the number wins
        chose = False
        ans = randint(1, 100)
        enemyAns = randint(1, 100)
        winner = False
        print("Welcome to the block mini game.")
        while not chose:
            playerAns = int(input("Choose a number between 1 and 100 "))
            if playerAns < 1 or playerAns > 100:
                print("You can't choose that number.")
            else:
                if playerAns < ans:
                    playA = ans-playerAns
                else:
                    playA = playerAns - ans
                if enemyAns < ans:
                    enemyA = ans-enemyAns
                else:
                    enemyA = enemyAns-ans

                if enemyA < playA:
                    #Enemy is closer
                    print("The number was", ans, "and the enemy guessed", enemyAns,"meaning that you lost")
                elif enemyA == playA:
                    print("You guys both tied. This means that you lost your turn and now the enemy will attack.")
                else:
                    #Player is closer
                    print("The number was", ans, "and the enemy guessed", enemyAns, "meaning that you won.")
                    winner = True
                return winner


    # Define enemy's attack behavior
    def enemyAttack(enemy, playerHealth):
        # Enemy can perform a normal attack or a special attack
        # The special attack has a chance to one-shot the player
        specialAttack = 100
        normalAttack = 30
        specialAttackPerc = randint(1, 100)
        print("Enemy Special Attack Number:", specialAttackPerc)
        if specialAttackPerc <= 7:
            #Special Attack happens
            print("You were hit by the enemy's special attack for", specialAttack, "damage")
            playerHealth-=specialAttack
    
        else:
            #Normal attack happens
            print("You were hit by the enemy's attack for", normalAttack, "damage")
            playerHealth-=normalAttack
        
        if playerHealth <= 0:
            print("You were killed. GG")
            playerHealth = 0

        else:
            print("You are at", playerHealth, "health")

        return playerHealth
    
    # Define a method to visualize the enemy
    def enemyLook(enemy):
        return " x "
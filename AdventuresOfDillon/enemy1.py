from random import randint
import math as m

class enemy1:
    def __init__(enemy, name, damage, health):
        enemy.name = name
        enemy.damage = damage
        enemy.health = health

    def __str__(enemy):
        return f"Name: {enemy.name}, Damage: {enemy.damage}, Health: {enemy.health}"
    
    def blockGame(enemy):
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


        
    def enemyAttack(enemy, playerHealth):
        #Enemy has normal + super attack (Has chance to one shot player)
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
    

    def enemyLook(enemy):
        return "x "
#!/usr/bin/env python3

from math import gamma

class gameCharacter:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def lifeCheck(self):
        if self.life <= 0:
            print(self.name + " has given up!")
        else:
            print(self.name + " is still fighting!")

class Player(gameCharacter):
    def attack(self):
        print(self.name + " kicks the enemy.")

class Enemy(gameCharacter):
    def attack(self):
        print(self.name + " breathes fire!")

def fight(character, target, damage):
    print("\n\n")
    character.attack()
    target.life -= damage
    print(target.name + " takes " + str(damage) + " damage!")
    print(target.name + " has " + str(target.life) + " life remaining.")
    target.lifeCheck()

player1 = Player("Mario", 155)
enemy1 = Enemy("Venom", 200)

print(player1.name + " life: " + str(player1.life))
print(enemy1.name + " life: " + str(enemy1.life))

fight(player1, enemy1, 151)
fight(enemy1, player1, 200)
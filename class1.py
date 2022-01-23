#!/usr/bin/env python3

class gameCharacter:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def attack(self):
        print(self.name + " kicks the enemy.")

    def life_check(self):
        if self.life <= 0:
            print(self.name + " was defeated.")
        else:
            print(self.name + " is still in the fight!")

class gameEnemy:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def attack(self):
        print(self.name + " attacks the heores.")

    def life_check(self):
        if self.life <= 0:
            print(self.name + " was defeated.")
        else:
            print(self.name + " is still in the fight!")

player1 = gameCharacter("Bobbi", 23)
player2 = gameCharacter("Betta", 20)

print(player1.name + " life: " + str(player1.life))
print(player2.name + " life: " + str(player2.life))

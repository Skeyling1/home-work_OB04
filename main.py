# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.

class Fighter:
    def __init__(self, Weapon):
        self.weapon = Weapon()

    def changeWeapon(self, Weapon):
        self.weapon = Weapon()


class Monster:
    pass

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("\nБоец выбирает меч.")
        print("Боец наносит удар мечом.")
        print("Монстр побежден!")

class Bow(Weapon):
    def attack(self):
        print("\nБоец выбирает лук.")
        print("Боец разит из лука.")
        print("Монстр побежден!")


figh1 = Fighter(Sword)

figh1.weapon.attack()

figh1.changeWeapon(Bow)

figh1.weapon.attack()
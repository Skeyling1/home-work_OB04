# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.

class Fighter:
    pass

class Monster:
    pass

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
# - Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`.
# Каждый из этих классов реализует метод `attack()` своим уникальным способом.



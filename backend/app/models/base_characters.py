class BaseCharacter:
    def __init__(self, name: str, stats: dict, abilities: list):
        self.name = name
        self.stats = stats
        self.abilities = abilities
        self.character_class = self.__class__.__name__

    def get_info(self):
        return {
            "name": self.name,
            "class": self.character_class,
            "stats": self.stats,
            "abilities": self.abilities
        }

class Alchemist(BaseCharacter):
    def __init__(self, name: str):
        stats = {"hp": 10, "damage": 3, "defense": 2, "speed": 4}
        abilities = ["Potion Mastery (passive)", "Transmute (active)"]
        super().__init__(name, stats, abilities)

class Warrior(BaseCharacter):
    def __init__(self, name: str):
        stats = {"hp": 14, "damage": 4, "defense": 4, "speed": 2}
        abilities = ["Battle Hardened (passive)", "Power Strike (active)"]
        super().__init__(name, stats, abilities)

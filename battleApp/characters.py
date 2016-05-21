import random

class Creature:
    def __init__(self, name : str, health: int):
        self.name = name
        self.health = health 

    def defensive_roll(self):
        return random.randint(1,12) * self.health 

    def attack(self, Creature):
        my_roll = self.defensive_roll()
        other_roll = Creature.defensive_roll()
        if (my_roll > other_roll):
            Creature.damage(my_roll)
        else:
            self.damage(other_roll/2)

    def damage(self, damage : int):
        self.health = self.health - damage
    def __repr__(self):
        return "{}: health {}".format(self.name, self.health)

class Soldier(Creature):
    pass

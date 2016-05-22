import random

class Creature:
    def __init__(self, name : str, health: int, strength: int):
        self.name = name
        self.health = health 
        self.strength = strength

    def defensive_roll(self):
        return random.randint(1,12) * self.health *self.strength 

    def use_powerup(self, Powerups):
        print("using powerup")
        if type(Powerups) == type(HealthBoost):
            self.health += Powerups.power()
            print("You used {}, your health is now {}".format(Powerups.name, self.health))
        elif Powerups == StrengthBoost:
            self.strength *= Powerups.power()
            print("You used {], your strength is now {}".format(Powerups.name, self.strength))


    def attack(self, Creature):
        my_roll = self.defensive_roll()
        other_roll = Creature.defensive_roll()
        if (my_roll > other_roll):
            Creature.damage(my_roll)
            print("You dealt {} damage!".format(my_roll))
        else:
            self.damage(other_roll/2)
            print("You got hurt -{}".format(other_roll/2))

    def damage(self, damage : int):
        self.health = self.health - damage

    def __repr__(self):
        return "{}: health {}".format(self.name, self.health)

class Soldier(Creature):
    pass

class Dragon(Creature):
    def __init__(self, name, health,strength, scaliness, can_breath_fire):
        super().__init__(name, health, strength)
        self.scaliness = scaliness
        self.can_breath_fire = can_breath_fire

    def defensive_roll(self):
        return super().defensive_roll() if (not self.can_breath_fire) else super().defensive_roll() * self.scaliness
    

class Powerups():
    def __init__(self, name):
        self.name = name

class HealthBoost(Powerups):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power
    
    def __repr__(self):
        return ("Health boost of {}".format(self.power))

class StrengthBoost(Powerups):
    def __init__(self,name, power):
        super().__init__(name)
        self.power = power

    def __repr__(self):
        return ("Strength boos of {}".format(self.power))

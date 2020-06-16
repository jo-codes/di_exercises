# Exercise 1 : Object Oriented Star Wars

import random
import statistics
from abc import ABC, abstractmethod


# class Powers(ABC):
#     @abstractmethod
#     def train(self, power, wisdom):
#         wisdom += random.randint(10, 20)
#         power += random.randint(5, 15)

#     @abstractmethod
#     def fight(self, opponent, power, wisdom):
#         hit_points = statistics.harmonic_mean([power, wisdom])
#         opponent.health -= hit_points

# I'm going to write the program without the above abstract classes, and then rewrite with them after


class ForceWielder():
    def __init__(self, name):
        self.name = name
        self.power = random.randint(1, 15)
        self.wisdom = random.randint(1, 15)
        self.total_power = statistics.harmonic_mean([self.power, self.wisdom])
        self.is_jedi = bool

    def merge_power(self):
        self.total_power = statistics.harmonic_mean([self.power, self.wisdom])

    def train(self):
        self.wisdom += random.randint(10, 20)
        self.power += random.randint(5, 15)
        self.merge_power()
        print(f"{self.name} has trained and grown stronger!")

    def make_sith(self):
        self.is_jedi = False
        print(f"{self.name} has gone over to the darkside!")
        self.name = f"Darth {self.name}"
        print(f"He is now {self.name}")
        self.power += 10
        self.merge_power()
        print(f"{self.name} has gained 10 power points")
        return self

    def make_jedi(self):
        self.is_jedi = True
        print(f"{self.name} has seen the light!")
        self.name = f"Sir {self.name}"
        print(f"He is now {self.name}")
        self.wisdom += 10
        self.merge_power()
        print(f"{self.name} has gained 10 wisdom points")
        return self

    def fight(self, opponent):
        self.lose = bool
        if opponent.total_power > self.total_power:
            self.lose = True
            print(f"{self.name} has lost..")
        else:
            self.lose = False
            print(f"{self.name} has won the fight")

        if self.is_jedi:
            self.train()
        elif not self.is_jedi and not self.lose:
            self.train()

        if self.lose:
            return "lose"
        else:
            return "win"


luke = ForceWielder("luke").make_jedi()
anniken = ForceWielder("anniken").make_jedi()
ray = ForceWielder("ray").make_jedi()
mole = ForceWielder("mole").make_sith()
vader = ForceWielder("vader").make_sith()
badguy = ForceWielder("badguy").make_sith()


arr_of_jedi = [luke, anniken, ray]
arr_of_badguys = [mole, vader, badguy]


fights = 0
while len(arr_of_badguys) != 0:
    fights += 1
    if fights >= 100:
        print("All is lost...")
        break

    dark_fighter = arr_of_badguys[0]
    light_fighter = arr_of_jedi[0]
    if light_fighter.fight(dark_fighter) == "lose":
        arr_of_jedi.insert(0, arr_of_jedi.pop(-1))
    else:
        print(f"{dark_fighter.name} has been defeated")
        arr_of_badguys.pop(0)

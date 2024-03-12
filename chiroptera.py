import random
from mammals import Mammals


class Chiroptera(Mammals):
    def __init__(self, mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism, flight_adaptations, nocturnal_habits, varied_diet):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.flight_adaptations = flight_adaptations
        self.nocturnal_habits = nocturnal_habits
        self.varied_diet = varied_diet
        self.representative = random.choice(['Vampire Bat', 'Fruit Bat', 'Flying Fox'])

    def echolocate(self):
        pass

    def roost(self):
        pass

    def groom(self):
        pass

def main():
    bat = Chiroptera(True, True, True, True, True, True, True, True, True)
    print(bat.representative)
    print(bat.echolocate())
    print(bat.roost())
    print(bat.groom())

if __name__ == "__main__":
    main()
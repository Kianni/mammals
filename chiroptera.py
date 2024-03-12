import random
from mammals import Mammals


class Chiroptera(Mammals):
    def __init__(
            self, 
            mammary_glands, 
            hair_fur, 
            warm_bloodedness, 
            viviparity, 
            middle_ear_bones, 
            sexual_dimorphism, 
            flight_adaptations, 
            nocturnal_habits, 
            varied_diet,
            representative=None):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.flight_adaptations = flight_adaptations
        self.nocturnal_habits = nocturnal_habits
        self.varied_diet = varied_diet
        if representative is None:
            self.representative = random.choice(['Fruit Bat', 'Flying Fox', 'Microbat'])
        else:
            self.representative = representative

    def echolocate(self):
        pass

    def roost(self):
        pass

    def groom(self):
        pass

def main():
    vampire_bat = Chiroptera(True, True, True, True, True, True, True, True, True, "Vampire Bat")
    bat = Chiroptera(True, True, True, True, True, True, True, True, True)
    print(vampire_bat.representative)
    print(bat.representative)
    print(bat.echolocate())
    print(bat.roost())
    print(bat.groom())

if __name__ == "__main__":
    main()
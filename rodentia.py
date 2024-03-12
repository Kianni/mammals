import random
from mammals import Mammals


class Rodentia(Mammals):
    def __init__(
            self, 
            mammary_glands, 
            hair_fur, 
            warm_bloodedness, 
            viviparity, 
            middle_ear_bones, 
            sexual_dimorphism, 
            continuously_growing_incissors, 
            high_reproduction_rate,
            representative=None):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.continuously_growing_incissors = continuously_growing_incissors
        self.high_reproduction_rate = high_reproduction_rate
        if representative is None:
            self.representative = random.choice(["Mouse", "Squirrel", "Beaver"])
        else:
            self.representative = representative

    def gnaw(self):
        pass

    def burrow(self):
        pass

    def hoardFood(self):
        pass

def main():
    rodent = Rodentia(True, True, True, True, True, True, True, True)
    rat = Rodentia(True, True, True, True, True, True, True, True, "Rat")
    print(rodent.representative)
    print(rat.representative)
    print(rat.gnaw())
    print(rat.burrow())
    print(rat.hoardFood())

if __name__ == "__main__":
    main()
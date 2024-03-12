import random
from mammals import Mammals


class Artiodactyla(Mammals):
    def __init__(self, mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism, even_toed_ungulates, herbivorous_diet, digestive_system, representative):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.even_toed_ungulates = even_toed_ungulates
        self.herbivorous_diet = herbivorous_diet
        self.digestive_system = digestive_system
        self.representative = random.choice(['Deer', 'Cow', 'Pig','Giraffe'])

    def graze(self):
        pass

    def ruminate(self):
        pass

    def migrate(self):
        pass

def main():
    dear = Artiodactyla(True, True, True, True, True, True, True, True, True, "Dear")
    print(dear.representative)
    print(dear.graze())
    print(dear.ruminate())
    print(dear.migrate())

if __name__ == "__main__":
    main()
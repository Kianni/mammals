from mammals import Mammals


class Carnivora(Mammals):
    def __init__(self, mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism, teeth_for_tearing_flesh, good_sight, smell, limbs_to_pursuit_prey, representative):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.teeth_for_tearing_flesh = teeth_for_tearing_flesh
        self.good_sight = good_sight
        self.smell = smell
        self.limbs_to_pursuit_prey = limbs_to_pursuit_prey
        self.representative = "Lion" | "Wolf"

    def consumePrey(self):
        pass

    def communicate(self):
        pass

    def hunt(self):
        pass

def main():
    lion = Carnivora(True, True, True, True, True, True, True, True, True, True, "Lion")
    print(lion.representative)
    print(lion.hunt())
    print(lion.consumePrey())
    print(lion.communicate())

if __name__ == "__main__":
    main()
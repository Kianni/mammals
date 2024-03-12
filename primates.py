from mammals import Mammals


class Primates(Mammals):
    def __init__(self, mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism, developed_brain, social_behaviour, opposite_thumb, representative):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.developed_brain = developed_brain
        self.social_behaviour = social_behaviour
        self.opposite_thumb = opposite_thumb
        self.representative = 'Monkey'

    def socialize(self):
        pass

    def toolUse(self):
        pass

    def arborealMovement(self):
        pass

def main():
    monkey = Primates(True, True, True, True, True, True, True, True, True, "Monkey")
    print(monkey.representative)
    print(monkey.socialize())
    print(monkey.toolUse())
    print(monkey.arborealMovement())

if __name__ == "__main__":
    main()
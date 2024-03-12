from mammals import Mammals


class Rodentia(Mammals):
    def __init__(self, mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism, continuously_growing_incissors, high_reproduction_rate, representative):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.continuously_growing_incissors = continuously_growing_incissors
        self.high_reproduction_rate = high_reproduction_rate
        self.representative = "Mouse" | "Squirrel" | "Beaver"

    def gnaw(self):
        pass

    def burrow(self):
        pass

    def hoardFood(self):
        pass

def main():
    mouse = Rodentia(True, True, True, True, True, True, True, True, "Mouse")
    print(mouse.representative)
    print(mouse.gnaw())
    print(mouse.burrow())
    print(mouse.hoardFood())

if __name__ == "__main__":
    main()
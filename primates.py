# from carnivora import Carnivora
from mammals import Mammals
# from rodentia import Rodentia


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

    def become_prey(self, predator):
        from carnivora import Carnivora
        if isinstance(predator, Carnivora):
            # code to simulate becoming prey
            print(f"The {self.representative} has become prey for a {predator.representative}.")
        else:
            print(f"This animal is not dangerous for the {self.representative}.")

def main():
    from rodentia import Rodentia
    from carnivora import Carnivora 
    monkey = Primates(True, True, True, True, True, True, True, True, True, "Monkey")
    rat = Rodentia(True, True, True, True, True, True, True, True, "Rat")
    lion = Carnivora(True, True, True, True, True, True, True, True, True, True, "Lion")
    monkey.become_prey(rat)  # Monkey does not become prey for rat
    monkey.become_prey(lion)  # Monkey becomes prey for lion
    print(monkey.representative)
    print(monkey.socialize())
    print(monkey.toolUse())
    print(monkey.arborealMovement())

if __name__ == "__main__":
    main()
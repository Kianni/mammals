import random
from carnivora import Carnivora
from mammals import Mammals


class Artiodactyla(Mammals):
    def __init__(
            self, 
            mammary_glands, 
            hair_fur, 
            warm_bloodedness, 
            viviparity, 
            middle_ear_bones, 
            sexual_dimorphism, 
            even_toed_ungulates, 
            herbivorous_diet, 
            digestive_system,
            representative=None):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.even_toed_ungulates = even_toed_ungulates
        self.herbivorous_diet = herbivorous_diet
        self.digestive_system = digestive_system
        if representative is None:
            self.representative = random.choice(['Mouse', 'Cow', 'Pig','Giraffe'])
        else:
            self.representative = representative

    def graze(self):
        pass

    def ruminate(self):
        pass

    def migrate(self):
        pass

    def become_prey(self, predator):
        from carnivora import Carnivora
        if isinstance(predator, Carnivora):
            # code to simulate becoming prey
            print(f"The {self.representative} has become prey for a {predator.representative}.")
        else:
            print(f"{predator.representative} is not dangerous for the {self.representative}.")

def main():
    deer = Artiodactyla(True, True, True, True, True, True, True, True, True, "Deer")
    artiodactyl = Artiodactyla(True, True, True, True, True, True, True, True, True)
    print(artiodactyl.representative)
    print(deer.representative)
    deer.become_prey(Carnivora(True, True, True, True, True, True, True, True, True, True))
    print(deer.graze())
    print(deer.ruminate())
    print(deer.migrate())

if __name__ == "__main__":
    main()
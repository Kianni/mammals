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
        self.state = "born"
        if representative is None:
            self.representative = random.choice(['Mouse', 'Cow', 'Pig','Giraffe'])
        else:
            self.representative = representative
        # mark the birth of the animal
        self._change_state('born')


    def _change_state(self, new_state):
        self.state = new_state
        print(f"{self.representative} {self.state}")

    def graze(self):
        self._change_state('grazing')

    def migrate(self):
        self._change_state('migrating')

    # youngsters graze when good pasture appears
    def check_and_graze(self, pasture):
        if self.state == 'born' and pasture == True:
            self.graze()

    # proceed grazing or migrate beacuse of lack of pasture
    def migrate_if_no_pasture(self, pasture=False):
        if pasture:
            self.graze() # the arrow from grazing to grazing is not shown in the diagram
        else:
            self.migrate()

    

    def ruminate(self):
        pass


    def become_prey(self, predator):
        self.state = 'prey'
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
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
        self.state = ""
        self.offspring = []
        if representative is None:
            self.representative = random.choice(['Mouse', 'Cow', 'Pig','Giraffe'])
        else:
            self.representative = representative
        # mark the birth of the animal
        self._change_state('birth')


    def _change_state(self, new_state):
        self.state = new_state
        print(f"{self.representative} {self.state}")

    def graze(self):
        self._change_state('grazing')

    def migrate(self):
        self._change_state('migrating')

    # youngsters graze when good pasture appears
    def check_and_graze(self, pasture):
        if self.state == 'birth' and pasture == True:
            self.graze()

    # proceed grazing or migrate beacuse of lack of pasture
    def migrate_if_no_pasture(self, pasture=False):
        if pasture:
            self.graze() # the arrow from grazing to grazing is not shown in the diagram
        else:
            self.migrate()

    # reproduction
    def encounter_with_a_mate(self, mate):
        if self.state == 'grazing' and isinstance(mate, Artiodactyla) and mate.mammary_glands == 'well developed':
            self._change_state('reproduction')
            mate._change_state('reproduction')
            num = random.randint(1, 3)
            super().numberOfChildren(num)
            for i in range(num):
                offspring = Artiodactyla("vestigial", True, True, True, True, True, True, True, True, "Deer") 
                offspring.representative = f"Deer Jr {i+1}"
                self.offspring.append(offspring)
            print(f"{mate.representative} gave birth to {num} offsprings.")
            for offspring in self.offspring:
                print(f"{offspring.representative} was born.")
            self._change_state('grazing')
            mate._change_state('grazing')

    def ruminate(self):
        pass

    # threatened by a predator
    def approach_by_predator(self, predator):
        num = random.randint(1, 10)
        if self.state == 'grazing':
            if num % 2 == 0:
                print(f"{self.representative} successful escape from {predator.representative}.")
                self._change_state('grazing')
            else:
                print(f"{self.representative} was caught by {predator.representative}.")
                self.become_prey(predator)


    def become_prey(self, predator):
        self.state = 'prey'
        from carnivora import Carnivora
        if isinstance(predator, Carnivora):
            # code to simulate becoming prey
            print(f"The {self.representative} has become prey for a {predator.representative}.")
            self._change_state('death')
        else:
            print(f"{predator.representative} is not dangerous for the {self.representative}.")

    # become sick and either recover or die
    def become_sick(self):
        print(f"{self.representative} is sick.")
        if self.state == 'grazing':
            self._change_state('not healthy')
            num = random.randint(1, 100)
            if num % 3 == 0 or num % 2 == 0:
                self._change_state('recovered')
                self.graze()
            else:
                self._change_state('death')

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
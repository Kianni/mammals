import random
# from artiodactyla import Artiodactyla
from mammals import Mammals
# from primates import Primates
from rodentia import Rodentia


class Carnivora(Mammals):
    def __init__(self, mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism, teeth_for_tearing_flesh, good_sight, smell, limbs_to_pursuit_prey):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.teeth_for_tearing_flesh = teeth_for_tearing_flesh
        self.good_sight = good_sight
        self.smell = smell
        self.limbs_to_pursuit_prey = limbs_to_pursuit_prey
        self.representative = random.choice(["Lion", "Wolf"])

    def consumePrey(self):
        pass

    def communicate(self):
        pass

    def hunt(self, prey):
        from artiodactyla import Artiodactyla
        from primates import Primates
        if isinstance(prey, (Primates, Artiodactyla)):
            # code to simulate hunting behaviour
            print(f"For {self.representative} a {prey.representative} was tasty and nutricious.")
            pass
        else:
            print(f"{prey.representative} is not a prey for {self.representative}.")

def main():
    from artiodactyla import Artiodactyla
    from primates import Primates

    lion = Carnivora(True, True, True, True, True, True, True, True, True, True)
    chimp = Primates(True, True, True, True, True, True, True, True, True)
    deer = Artiodactyla(True, True, True, True, True, True, True, True, True)
    rat = Rodentia(True, True, True, True, True, True, True, True)
    print(lion.representative)
    lion.hunt(chimp)  # Lion hunts chimp
    lion.hunt(deer)  # Lion hunts deer
    lion.hunt(rat)  # Lion does not hunt rat
    print(lion.consumePrey())
    print(lion.communicate())

if __name__ == "__main__":
    main()
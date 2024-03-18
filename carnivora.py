import random
# from artiodactyla import Artiodactyla
from mammals import Mammals
# from primates import Primates
from rodentia import Rodentia


class Carnivora(Mammals):
    def __init__(
            self, 
            mammary_glands, 
            hair_fur, 
            warm_bloodedness, 
            viviparity, 
            middle_ear_bones, 
            sexual_dimorphism, 
            teeth_for_tearing_flesh, 
            good_sight, 
            smell, 
            limbs_to_pursuit_prey,
            representative=None
            ):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.teeth_for_tearing_flesh = teeth_for_tearing_flesh
        self.good_sight = good_sight
        self.smell = smell
        self.limbs_to_pursuit_prey = limbs_to_pursuit_prey
        self.data_api = self.get_API_data('Carnivora')
        self.representative = self.get_representative(representative)
        self.url_wiki = self.data_api[1] or "https://en.wikipedia.org/wiki/Carnivora"

    def get_representative(self, representative):
        if representative is None:
            representative = self.data_api[0]
            if representative is None:
                representative = random.choice(["Wolf", "Tiger", "Leopard", "Jaguar", "Cheetah", "Hyena", "Fox", "Bear"])
        return representative

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

    lion = Carnivora(True, True, True, True, True, True, True, True, True, True, "Lion")
    carnivore = Carnivora(True, True, True, True, True, True, True, True, True, True)
    chimp = Primates(True, True, True, True, True, True, True, True, True)
    deer = Artiodactyla(True, True, True, True, True, True, True, True, True)
    rat = Rodentia(True, True, True, True, True, True, True, True, "Rat")
    print(lion.representative)
    print(carnivore.representative)

    lion.hunt(chimp)  # Lion hunts chimp
    lion.hunt(deer)  # Lion hunts deer
    lion.hunt(rat)  # Lion does not hunt rat
    print(lion.consumePrey())
    print(lion.communicate())

    random_carnivore = Carnivora(True, True, True, True, True, True, True, True, True, True)
    print(random_carnivore.representative)
    print(random_carnivore.url_wiki)

if __name__ == "__main__":
    main()
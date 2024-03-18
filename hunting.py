from carnivora import Carnivora
from primates import Primates

class Hunting:
    def __init__(self, predator, prey):
        self.predator = predator
        self.prey = prey

    def main(self):
        self.predator.hunt(self.prey)
        self.prey.become_prey(self.predator)

if __name__ == "__main__":

    lion = Carnivora(True, True, True, True, True, True, True, True, True, True, "Lion")
    human = Primates(True, True, True, True, True, True, True, True, True, "Human")

    tragedic_hunt = Hunting(lion, human)
    tragedic_hunt.main()

    random_carnivora_api = Carnivora(True, True, True, True, True, True, True, True, True, True)
    random_primate_api = Primates(True, True, True, True, True, True, True, True, True)

    random_hunt = Hunting(random_carnivora_api, random_primate_api)
    random_hunt.main()

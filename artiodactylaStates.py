from enum import Enum
from artiodactyla import Artiodactyla
from carnivora import Carnivora

def main():
    # -> birth
    deer_male = Artiodactyla("vestigial", True, True, True, True, True, True, True, True, "Deer male")
    deer_female = Artiodactyla("well developed", True, True, True, True, True, True, True, True, "Deer female")

    class PastureCondition(Enum):
        APPEARANCE_OF_GOOD_PASTURE = True
        LACK_OF_PASTURE = False

    # birth -> grazing
    deer_male.check_and_graze(PastureCondition.APPEARANCE_OF_GOOD_PASTURE.value)
    
    # grazing -> grazing (no transition shown in the diagram)
    deer_male.migrate_if_no_pasture(PastureCondition.APPEARANCE_OF_GOOD_PASTURE.value)
    
    # grazing -> reproduction -> grazing
    deer_female.check_and_graze(PastureCondition.APPEARANCE_OF_GOOD_PASTURE.value)
    deer_male.encounter_with_a_mate(deer_female)

    offspring = deer_male.offspring[-1]
    offspring.check_and_graze(PastureCondition.APPEARANCE_OF_GOOD_PASTURE.value)
    offspring.become_sick()

    # grazing -> threatened -> [ death / grazing ]
    lion = Carnivora(True, True, True, True, True, True, True, True, True, True, "Lion")
    deer_male.approach_by_predator(lion)
    deer_female.approach_by_predator(lion)

    # grazing -> migration
    deer_male.migrate_if_no_pasture(PastureCondition.LACK_OF_PASTURE.value)


if __name__ == "__main__":
    main()

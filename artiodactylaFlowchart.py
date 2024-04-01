from enum import Enum
from artiodactyla import Artiodactyla
from carnivora import Carnivora

def main():
    class PastureCondition(Enum):
        APPEARANCE_OF_GOOD_PASTURE = True
        LACK_OF_PASTURE = False

    # -> birth
    deer_male = Artiodactyla("vestigial", True, True, True, True, True, True, True, True, "Deer")
    deer_invalid = Artiodactyla("nothing", True, True, True, True, True, True, True, True, "Deer")

    # flowchart: pasture is good -> "Deer grazing"
    deer_male.check_and_graze(PastureCondition.APPEARANCE_OF_GOOD_PASTURE.value)

    # flowchart: pasture is NOT good -> "Deer migrating"
    deer_male.migrate_if_no_pasture(PastureCondition.LACK_OF_PASTURE.value)
    # after finding good pasture, the deer will graze again

    # flowchart: approuching by the predator and maybe survive
    lion = Carnivora(True, True, True, True, True, True, True, True, True, True, "Lion")
    deer_male.approach_by_predator(lion)
    if deer_male.state == 'death':
        del deer_male
    # flowchart: become sick and maybe recover after that 
    else:
        deer_male.become_sick()


if __name__ == "__main__":
    main()
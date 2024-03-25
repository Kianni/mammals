from enum import Enum
from artiodactyla import Artiodactyla
from carnivora import Carnivora

def main():
    # -> birth
    deer = Artiodactyla(True, True, True, True, True, True, True, True, True, "Deer")
    
    class PastureCondition(Enum):
        APPEARANCE_OF_GOOD_PASTURE = True
        LACK_OF_PASTURE = False

    # birth -> grazing
    deer.check_and_graze(PastureCondition.APPEARANCE_OF_GOOD_PASTURE.value)

    # grazing -> grazing (no transition shown in the diagram)
    deer.migrate_if_no_pasture(PastureCondition.APPEARANCE_OF_GOOD_PASTURE.value)
    
    # grazing -> migration
    deer.migrate_if_no_pasture(PastureCondition.LACK_OF_PASTURE.value)


if __name__ == "__main__":
    main()

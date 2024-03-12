class Mammals:
    def __init__(self, mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism):
        self.mammary_glands = mammary_glands
        self.hair_fur = hair_fur
        self.warm_bloodedness = warm_bloodedness
        self.viviparity = viviparity
        self.middle_ear_bones = middle_ear_bones
        self.sexual_dimorphism = sexual_dimorphism

    def milk_production(self):
        return self.mammary_glands

    def change_fur(self, new_fur):
        self.hair_fur = new_fur

    def set_normal_temp(self, temp):
        self.warm_bloodedness = temp

    def numberOfChildren(self, children):
        self.viviparity = children

    def set_hearing_diapason(self, hearing):
        self.middle_ear_bones = hearing

    def set_diet(self, diet):
        self.diet = diet

    def set_parental_care_form(self, care):
        self.parental_care = care

def main():
    # Create an object of the Mammals class
    human = Mammals(2, "short", 98.6, 1, 3, "yes")
    print(human.milk_production())
    print(human.hair_fur)
    print(human.warm_bloodedness)
    print(human.viviparity)
    print(human.middle_ear_bones)

if __name__ == "__main__":
    main()
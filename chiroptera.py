from mammals import Mammals


class Chiroptera(Mammals):
    def __init__(self, mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism, flight_adaptations, nocturnal_habits, varied_diet, representative):
        super().__init__(mammary_glands, hair_fur, warm_bloodedness, viviparity, middle_ear_bones, sexual_dimorphism)
        self.flight_adaptations = flight_adaptations
        self.nocturnal_habits = nocturnal_habits
        self.varied_diet = varied_diet
        self.representative = 'Vampire Bat'

    def echolocate(self):
        pass

    def roost(self):
        pass

    def groom(self):
        pass
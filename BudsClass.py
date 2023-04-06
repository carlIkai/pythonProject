

class BudsClass():

    def __init__(self, strain: str, potency: float) -> None:
        self.strain = strain
        self.potency = potency

    def add_strain(self, new_strain: str) -> None:
        self.strain = new_strain

    def add_potency(self, new_potency: float) -> None:
        self.strain = new_potency

    def add_rating(self, new_rating: int) -> None:
        self.strain = new_rating

    def print_object(self) -> None:
        print("Strain: " + self.strain)
        print("Potency: " + str(self.potency))
        #print("Rating: " + str(self.rating))
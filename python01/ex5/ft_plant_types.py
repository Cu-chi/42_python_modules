class Plant:
    """A class representing a plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant object

        Args:
            name (str): Name of the plant
            height (int): Height of the plant
            age (int): Age of the plant
        """
        self.name: str = name
        self.height: int = height
        self._age: int = age

    def grow(self) -> None:
        """Grow the plant
        """
        self.height += 1

    def age(self) -> None:
        """Age the plant
        """
        self._age += 1

    def get_info(self) -> str:
        """info of the plant

        Returns:
            str: info of the plant
        """
        return (f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
                + f"{self._age} days")


class Flower(Plant):
    """A class representing a flower, inherits from Plant
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a Flower object

        Parameters:
            name (str): Flower name
            height (int): Flower height
            age (int): Flower age
            color (str): Flower color
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """make the flower bloom
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        """info of the plant

        Returns:
            str: info of the plant
        """
        info: str = super().get_info()
        return info + f", {self.color} color"


class Tree(Plant):
    """A class representing a tree, inherits from Plant
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Initialize a Tree object

        Parameters:
            name (str): Tree name
            height (int): Tree height
            age (int): Tree age
            trunk_diameter (int): Tree trunk diameter
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """print the produced shade
        """
        shade: int = self.trunk_diameter * 8
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> str:
        """info of the plant

        Returns:
            str: info of the plant
        """
        return super().get_info() + f", {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """A class representing a vegetable, inherits from Plant
    """
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Initialize a vegetable object

        Parameters:
            name (str): Vegetable name
            height (int): Vegetable height
            age (int): Vegetable age
            harvest_season (str): Vegetable harvest season
            nutritional_value (str): Vegetable nutritional value
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> str:
        """info of the plant

        Returns:
            str: info of the plant
        """
        info: str = super().get_info() + f", {self.harvest_season} harvest"
        info += f"\n{self.name} is rich in {self.nutritional_value}"
        return info


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    plants_data: list = [
        (Flower, "Rose", 25, 30, "red"),
        (Tree, "Oak", 500, 1825, 50),
        (Vegetable, "Tomato", 80, 90, "summer", "vitamin C"),
    ]
    plants: list = [plant[0](*plant[1:]) for plant in plants_data]
    for plant in plants:
        print()
        print(plant.get_info())
        if plant.__class__.__name__ == "Tree":
            plant.produce_shade()
        elif plant.__class__.__name__ == "Flower":
            plant.bloom()

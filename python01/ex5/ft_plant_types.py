class Plant:
    """A class representing a plant
    """
    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant object

        Args:
            name (str): Name of the plant
            height (int): Height of the plant
            age (int): Age of the plant
        """
        self.name = name
        self.height = height
        self._age = age

    def grow(self):
        """Grow the plant
        """
        self.height += 1

    def age(self):
        """Age the plant
        """
        self._age += 1

    def get_info(self) -> str:
        """info of the plant

        Returns:
            str: info of the plant
        """
        return (f"{self.name} ({type(self).__name__}): {self.height}cm, "
                + f"{self._age} days")


class Flower(Plant):
    """
    A class representing a flower, inherits from Plant

    Attributes:
        name (str): Flower name
        height (int): Flower height
        _age (int): Flower age
        color (str): Flower color
    """
    def __init__(self, name: str, height: int, age: int, color: str):
        """
        Initialize a Flower object

        Parameters:
            name (str): Flower name
            height (int): Flower height
            age (int): Flower age
            color (str): Flower color
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """make the flower bloom
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        """info of the plant

        Returns:
            str: info of the plant
        """
        info = super().get_info()
        return info + f", {self.color} color"


class Tree(Plant):
    """
    A class representing a tree, inherits from Plant

    Attributes:
        name (str): Tree name
        height (int): Tree height
        _age (int): Tree age
        trunk_diameter (int): Tree trunk diameter
    """
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
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

    def produce_shade(self):
        """print the produced shade
        """
        shade = self.height * self.trunk_diameter / 100
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> str:
        """info of the plant

        Returns:
            str: info of the plant
        """
        info = super().get_info() + f", {self.trunk_diameter}cm diameter"
        return info


class Vegetable(Plant):
    """
    A class representing a vegetable, inherits from Plant

    Attributes:
        name (str): Vegetable name
        height (int): Vegetable height
        _age (int): Vegetable age
        harvest_season (str): Vegetable harvest season
        nutritional_value (str): Vegetable nutritional value
    """
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str):
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
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        """info of the plant

        Returns:
            str: info of the plant
        """
        info = super().get_info() + f", {self.harvest_season} harvest"
        info += f"\n{self.name} is rich in {self.nutritional_value}"
        return info


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    plants_data = [
        (Flower, "Rose", 10, 8, "red"),
        (Flower, "Sunflower", 15, 20, "yellow"),
        (Tree, "Oak", 620, 2300, 80),
        (Tree, "Coconut", 800, 5400, 40),
        (Vegetable, "Tomato", 70, 80, "summer", "vitamin C"),
        (Vegetable, "Pumpkin", 20, 30, "autumn", "vitamin E"),
    ]
    plants = [plant[0](*plant[1:]) for plant in plants_data]
    for plant in plants:
        print(plant.get_info())
        if type(plant).__name__ == "Tree":
            plant.produce_shade()
        elif type(plant).__name__ == "Flower":
            plant.bloom()

class Plant:
    """
    A class representing a plant

    Attributes:
        name (str): Plant name
        height (int): Plant height
        age (int): Plant age
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant object

        Parameters:
            name (str): Plant name
            height (int): Plant height
            age (int): Plant age
        """
        self.name = name
        self.height = height
        self._age = age

    def grow(self):
        """
        Grow the plant
        """
        self.height += 1
        return

    def age(self):
        """
        Age the plant
        """
        self._age += 1
        return

    def get_info(self):
        """
        Print info of the plant
        """
        print(f"{self.name}: {self.height}cm, {self._age} days old")


if __name__ == "__main__":
    plants_data = [
        ("Rose", 10, 8),
        ("Cactus", 15, 120),
        ("Sunflower", 15, 20),
        ("Tulip", 8, 12),
        ("Iris", 6, 4),
    ]
    total_plants = 0
    print("=== Plant Factory Output ===")
    for plant_data in plants_data:
        total_plants += 1
        name, height, age = plant_data
        print(f"Created: {name} ({height}cm, {age} days)")
    print(f"\nTotal plants created: {total_plants}")

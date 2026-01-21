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
        print(f"Created: {name} ({height}cm, {age} days)")
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
    print("=== Plant Factory Output ===")
    plants_data = [
        ("Rose", 10, 8),
        ("Cactus", 15, 120),
        ("Sunflower", 15, 20),
        ("Tulip", 8, 12),
        ("Iris", 6, 4),
    ]
    plants = [Plant(*plant_data) for plant_data in plants_data]
    total_plants = 0
    for plant_data in plants_data:
        total_plants += 1
    print(f"\nTotal plants created: {total_plants}")

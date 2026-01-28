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
        print(f"Created: {name} ({height}cm, {age} days)")
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

    def get_info(self) -> None:
        """Print info of the plant
        """
        print(f"{self.name}: {self.height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants_data: list = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    plants: list = [Plant(*plant_data) for plant_data in plants_data]
    total_plants: int = 0
    for plant_data in plants_data:
        total_plants += 1
    print(f"\nTotal plants created: {total_plants}")

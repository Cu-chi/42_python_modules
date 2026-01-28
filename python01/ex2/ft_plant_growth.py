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

    def get_info(self) -> None:
        """Print info of the plant
        """
        print(f"{self.name}: {self.height}cm, {self._age} days old")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    base_age: int = rose._age
    print("=== Day 1 ===")
    rose.get_info()
    for i in range(6):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose._age - base_age}cm")

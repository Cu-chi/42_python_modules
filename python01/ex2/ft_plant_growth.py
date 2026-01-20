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
    rose = Plant("Rose", 25, 30)
    base_age = rose._age
    print("=== Day 1 ===")
    rose.get_info()
    for i in range(6):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose._age - base_age}cm")

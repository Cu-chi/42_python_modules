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
        self.age = age


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    ("=== Garden Plant Registry ===")
    for i in range(3):
        print(f"{plants[i].name}: {plants[i].height}cm, {plants[i].age} days "
              "old")

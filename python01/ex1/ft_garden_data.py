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

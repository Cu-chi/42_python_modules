class Garden:
    """A class representing a Garden
    """
    def __init__(self, garden_name: str,
                 stats: 'GardenManager.GardenStats') -> None:
        """Initialize a Garden object

        Args:
            garden_name (str): Name of the garden
            stats (GardenManager.GardenStats): GardenStats class
        """
        self.garden_name: str = garden_name
        self.plants: list[Plant] = []
        self.stats: GardenManager.GardenStats = stats()

    def add_plant(self, plant: 'Plant') -> None:
        """add a plant to the garden

        Args:
            plant (Plant): The Plant object
        """
        print(f"Added {plant.name} to {self.garden_name}'s garden")
        self.plants = self.plants + [plant]
        self.stats.added += 1
        if plant.__class__ == Plant:
            self.stats.regular += 1
        elif plant.__class__ == FloweringPlant:
            self.stats.flowering += 1
        elif plant.__class__ == PrizeFlower:
            self.stats.prize_flower += 1

    def grow_all(self) -> None:
        """Grow all plants in the garden
        """
        print(f"{self.garden_name} is helping all plants grow...")
        for plant in self.plants:
            self.stats.total_growth += 1
            plant.grow()

    def report(self) -> None:
        """Print the stats report of the garden
        """
        print(f"=== {self.garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f" - {plant.get_info()}")
        print()
        print(self.stats.report())


class GardenManager:
    """A class representing a Garden Manager
    """
    class GardenStats:
        """A helper class used to make stats on garden
        """
        def __init__(self) -> None:
            """Initialize a GardenStats object
            """
            self.added: int = 0
            self.total_growth: int = 0
            self.regular: int = 0
            self.flowering: int = 0
            self.prize_flower: int = 0
            self.score: int = 0

        def report(self) -> str:
            """Generate the string for the garden report

            Returns:
                str: report
            """
            report: str = f"Plants added: {self.added}"
            report += f", Total growth: {self.total_growth}cm"
            report += f"\nPlant types: {self.regular} regular"
            report += f", {self.flowering} flowering"
            report += f", {self.prize_flower} prize flowers"
            return report

    def __init__(self, gardens: list[Garden]) -> None:
        """Initialize a GardenManager object

        Args:
            gardens (list[Garden]): list of gardens
        """
        self.gardens: list[Garden] = gardens

    @classmethod
    def create_garden_network(cls, gardens_data: list) -> 'GardenManager':
        """Create and initialize a garden network
        it takes the data of gardens and create a clean list of Garden objects

        Args:
            gardens_data (list): list of unformatted gardens

        Returns:
            GardenManager: The GardenManager object created
        """
        gardens: list[Garden] = []
        for row in gardens_data:
            name: str = row[0]
            plant_class: type = row[1]
            plant_data: tuple = row[2:]
            plant_object: Plant = plant_class(*plant_data)
            garden: Garden | None = GardenManager.get_garden(gardens, name)
            if (garden is None):
                garden = Garden(name, GardenManager.GardenStats)
                gardens = gardens + [garden]
            garden.add_plant(plant_object)
        return cls(gardens)

    def add_plant_to(self, plant: 'Plant' | 'FloweringPlant' | 'PrizeFlower',
                     garden_name: str) -> None:
        """Add a plant to the garden of the name specified

        Args:
            plant (Plant | FloweringPlant | PrizeFlower): the Plant object
            garden_name (str): The Garden Name
        """
        garden: Garden = GardenManager.get_garden(self.gardens, garden_name)
        if garden:
            garden.add_plant(plant)

    def get_total_managed(self) -> int:
        """Get the number of managed gardens

        Returns:
            int: number of managed gardens
        """
        total_managed: int = 0
        for _ in self.gardens:
            total_managed += 1
        return total_managed

    def grow_all(self, garden_name: str) -> None:
        """Grow all plants of the garden name specified

        Args:
            garden_name (str): Garden name
        """
        garden: Garden = GardenManager.get_garden(self.gardens, garden_name)
        if garden:
            garden.grow_all()

    def report(self, garden_name: str) -> None:
        """Generate the stats report of the garden name specified

        Args:
            garden_name (str): Garden name
        """
        garden: Garden = GardenManager.get_garden(self.gardens, garden_name)
        if garden:
            garden.report()

    def calculate_scores(self) -> str:
        """Calculate the scores of gardens

        Returns:
            str: the formated scores
        """
        result: str = ""
        first: bool = True
        for garden in self.gardens:
            if first:
                result += garden.garden_name + ": "
                first = False
            else:
                result += ", " + garden.garden_name + ": "
            score: int = 0
            for plant in garden.plants:
                score += plant.height
            result += f"{score}"
        return result

    @staticmethod
    def get_garden(gardens: list[Garden], garden_name: str) -> Garden | None:
        """Get a garden from its name in a list of garden

        Args:
            gardens (list[Garden]): list of gardens object
            garden_name (str): garden name to get

        Returns:
            Garden | None: Garden object or None if doesn't exist
        """
        for garden in gardens:
            if garden.garden_name == garden_name:
                return garden
        return None

    def validate_height(self) -> bool:
        """Check all height of all plants of all gardens

        Returns:
            bool: True if all height are valid, False if not
        """
        status: bool = True
        for garden in self.gardens:
            for plant in garden.plants:
                if plant.height < 0:
                    print(f"Plant {plant.name} of {garden.garden_name}'s"
                          f" garden has height of {plant.height} (must be >0)")
                    status = False
        return status


class Plant:
    """A class representing a plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant object

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
        print(f"{self.name} grew 1cm")
        self.height += 1

    def age(self) -> None:
        """Age the plant
        """
        self._age += 1

    def get_info(self) -> str:
        """Print info of the plant
        """
        return (f"{self.name}: {self.height}cm, "
                + f"{self._age} days")


class FloweringPlant(Plant):
    """A class representing a Flowering Plant
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a FloweringPlant object

        Args:
            name (str): Name of the plant
            height (int): Height of the plant
            age (int): Age of the plant
            color (str): Color of the plant
        """
        super().__init__(name, height, age)
        self.color: str = color

    def get_info(self) -> str:
        """Print info of the plant
        """
        return super().get_info() + f", {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """A class representing a Prize flower
    """
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize: int) -> None:
        """Initilialize a PrizeFlower object

        Args:
            name (str): Name of the plant
            height (int): Height of the plant
            age (int): Age of the plant
            color (str): Color of the plant
            prize (int): Prize of the plant
        """
        super().__init__(name, height, age, color)
        self.prize: int = prize

    def get_info(self) -> str:
        """Print info of the plant
        """
        return super().get_info() + f", Prize points: {self.prize}"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    gardens_data: list = [
        ("Alice", Plant, "Oak Tree", 620, 2300),
        ("Alice", FloweringPlant, "Rose", 10, 8, "red"),
        ("Alice", PrizeFlower, "Sunflower", 15, 20, "yellow", 10),
        ("Bob", FloweringPlant, "Tulip", 25, 7, "pink")
    ]
    manager = GardenManager.create_garden_network(gardens_data)
    print()
    manager.grow_all("Alice")
    print()
    manager.report("Alice")
    print()
    print(f"Height validation test: {manager.validate_height()}")
    print(f"Garden scores - {manager.calculate_scores()}")
    print(f"Total gardens managed: {manager.get_total_managed()}")

class WateringError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class PlantHealthError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class GardenError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class Plant:
    """A class representing a plant
    """
    def __init__(self, name: str, height: int, age: int, water: int,
                 sun: int) -> None:
        """Initialize a Plant object

        Args:
            name (str): Name of the plant
            height (int): Height of the plant
            age (int): Age of the plant
            water (int): Water level of the plant
            sun (int): Sun level of the plant
        """
        if name == "":
            raise GardenError("Plant name cannot be empty!")
        self.name: str = name
        if height < 0:
            raise GardenError("Plant height cannot be negative!")
        self.height: int = height
        if age < 0:
            raise GardenError("Plant age cannot be negative!")
        self._age: int = age
        self.water: int = water
        self.sun: int = sun

    def get_info(self) -> str:
        """Print info of the plant
        """
        return (f"{self.name}: {self.height}cm, "
                + f"{self._age} days")


class GardenManager:
    """A class representing a Garden Manager
    """
    def __init__(self, plants: list) -> None:
        """Initialize a GardenManager object

        Args:
            plants (list): plants list
        """
        self.__plants: list[Plant] = []
        self.tank: int = 500
        for plant_data in plants:
            self.add_plant(plant_data[0], plant_data[1], plant_data[2],
                           plant_data[3], plant_data[4])

    def add_plant(self, name: str, height: int, age: int, water: int,
                  sun: int) -> None:
        try:
            self.__plants = self.__plants + [Plant(name, height, age, water,
                                                   sun)]
            print(f"Added {name} successfully")
        except GardenError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, fail=False) -> None:
        print("Opening watering system")
        try:
            for plant in self.__plants:
                print(f"Watering {plant.name} - ", end="")
                if not fail:
                    print("success")
                else:
                    print("failure")
                    raise WateringError(f"failed to water {plant.name}")
        except WateringError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def get_all_plants(self) -> list[Plant]:
        return self.__plants

    def check_water_tank(self) -> None:
        if self.tank <= 0:
            raise GardenError("Not enough water in tank")

    @staticmethod
    def check_plant_health(plant: Plant) -> None:
        if plant.water > 10:
            raise PlantHealthError(
                f"Water level {plant.water} is too high (max 10)")
        elif plant.water < 1:
            raise PlantHealthError(
                f"Water level {plant.water} is too low (min 1)")
        if plant.sun > 12:
            raise PlantHealthError(
                f"Sunlight hours {plant.sun} is too high (max 12)")
        elif plant.sun < 2:
            raise PlantHealthError(
                f"Sunlight hours {plant.sun} is too low (min 2)")
        print(f"{plant.name}: healthy (water: {plant.water}, "
              f"sun: {plant.sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    plants_data: list = [
        ("", 620, 2300, 5, 8),
        ("Rose", -10, 8, 5, 8),
        ("Sunflower", 15, -20, 5, 8),
        ("Tulip", 25, 7, 5, 80),
        ("Rose", 10, 8, 5, 8)
    ]
    print("Adding plants to garden...")
    garden_manager: GardenManager = GardenManager(plants_data)
    print("\nWatering plants...")
    garden_manager.water_plants()
    garden_manager.water_plants(True)
    print("Checking plant health...")
    for plant in garden_manager.get_all_plants():
        try:
            garden_manager.check_plant_health(plant)
        except PlantHealthError as e:
            print(f"Error checking {plant.name}: {e}")
    print("\nTesting error recovery...")
    garden_manager.tank = 0
    try:
        garden_manager.check_water_tank()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

class GardenError(Exception):
    def __init__(self, message: str, *args) -> None:
        super().__init__(*args)
        self.message: str = message


class PlantError(GardenError):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class WaterError(GardenError):
    def __init__(self, *args) -> None:
        super().__init__(*args)


def plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_error_types() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e.message}")
    print("\nTesting WaterError...")
    try:
        water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e.message}")
    print("\nTesting catching all garden errors...")
    try:
        plant_error()
    except GardenError as e:
        print(f"Caught garden error: {e.message}")
    try:
        water_error()
    except GardenError as e:
        print(f"Caught garden error: {e.message}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_error_types()

def water_plants(plant_list) -> None:
    print("Opening watering system")
    for plant in plant_list:
        if plant is not None:
            print(f"Watering {plant}")
        else:
            raise Exception("Cannot water None - invalid plant!")


def test_watering_system() -> None:
    valid_plants: list[str] = ["Rose", "Sunflower", "Tomato", "Tulip"]
    invalid_plants: list[str | None] = ["Rose", None, "Tomato", "Tulip"]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    try:
        water_plants(valid_plants)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!\n")
    print("Testing with error...")
    try:
        water_plants(invalid_plants)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)\n")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

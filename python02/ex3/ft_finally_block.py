def water_plants(plant_list):
    print("Opening watering system")
    for plant in plant_list:
        if plant is not None:
            print(f"Watering {plant}")
        else:
            raise Exception("Cannot water None - invalid plant!")


def test_watering_system():
    valid_plants = ["Rose", "Sunflower", "Tomato", "Tulip"]
    invalid_plants = ["Rose", None, "Tomato", "Tulip"]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    try:
        water_plants(valid_plants)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        
    try:
        water_plants(invalid_plants)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_watering_system()

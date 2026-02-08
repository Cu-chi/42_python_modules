def method_1() -> None:
    import alchemy.elements
    print("Method 1 - Multiple imports:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")


def method_2() -> None:
    from alchemy.elements import create_water
    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")


def method_3() -> None:
    from alchemy.potions import healing_potion as heal
    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")


def method_4() -> None:
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


def main() -> None:
    print("\n=== Import Transmutation Mastery ===\n")
    method_1()
    print()
    method_2()
    print()
    method_3()
    print()
    method_4()
    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()

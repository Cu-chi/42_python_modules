import sys


class InventoryError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


def arg_split(input_string: str) -> None | tuple[str, str]:
    dot_pos: int = -1
    i = 0
    for char in input_string:
        if char == ":":
            dot_pos = i
            break
        i += 1
    if dot_pos == -1:
        return None
    return (input_string[:dot_pos], input_string[(dot_pos + 1):])


def create_dict(args: list[str]) -> dict | None:
    arg_dict: dict = {}
    for arg in args:
        key: str
        value: str
        key, value = arg_split(arg)
        if key is None or value is None:
            raise InventoryError(f"error parsing arg '{arg}'")
        amount: int = int(value)
        if (amount <= 0):
            raise InventoryError(f"invalid amount of '{key}': {value}")
        arg_dict.update({key: amount})
    return arg_dict


def get_most_abundant(inv: dict[str, int]) -> None | str:
    most_abundant: str = None
    for key, value in inv.items():
        if most_abundant is None or value > inv[most_abundant]:
            most_abundant = key
    return most_abundant


def get_least_abundant(inv: dict[str, int]) -> None | str:
    least_abundant: str = None
    for key, value in inv.items():
        if least_abundant is None or value < inv[least_abundant]:
            least_abundant = key
    return least_abundant


def create_categories(inv: dict[str, int],
                      total_items: int) -> dict[str, dict[str, int]]:
    categories: dict[str, dict[str, int]] = {
        "Common": {},
        "Moderate": {},
        "Scarce": {}
    }
    for key, value in inv.items():
        percentage: float = value / total_items
        if percentage < 0.3:
            categories["Scarce"].update({key: value})
        elif percentage < 0.5:
            categories["Moderate"].update({key: value})
        else:
            categories["Common"].update({key: value})
    return categories


def get_restock_needed(inv: dict[str, int]) -> list[str]:
    restock_needed: list[str] = []
    for key, value in inv.items():
        if value <= 1:
            restock_needed = restock_needed + [key]
    return restock_needed


def main() -> None:
    inventory: dict
    try:
        inventory = create_dict(sys.argv[1:])
        print("=== Inventory System Analysis ===")
        total_items = 0
        for value in inventory.values():
            total_items += value
        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {len(inventory.keys())}")

        print("\n=== Current Inventory ===")
        for key, value in inventory.items():
            print(f"{key}: {value}", end="")
            if value > 1:
                print(" units ", end="")
            else:
                print(" unit ", end="")
            print(f"({value/total_items*100:.1f}%)")

        print("\n=== Inventory Statistics ===")
        most_abundant: None | str = get_most_abundant(inventory)
        if most_abundant is not None:
            print(f"Most abundant: {most_abundant}", end="")
            if inventory[most_abundant] > 1:
                print(f" ({inventory[most_abundant]} units)")
            else:
                print(f" ({inventory[most_abundant]} unit)")
        least_abundant: None | str = get_least_abundant(inventory)
        if least_abundant is not None:
            print(f"Least abundant: {least_abundant}", end="")
            if inventory[least_abundant] > 1:
                print(f" ({inventory[least_abundant]} units)")
            else:
                print(f" ({inventory[least_abundant]} unit)")

        print("\n=== Inventory Categories ===")
        categories: dict[str, dict[str, int]] = create_categories(inventory,
                                                                  total_items)
        for categorie in categories.keys():
            if len(categories[categorie]) > 0:
                print(f"{categorie}: {categories[categorie]}")
        print("\n=== Management Suggestions ===")
        print(f"Restock needed: {get_restock_needed(inventory)}")
        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionnary keys: {inventory.keys()}")
        print(f"Dictionnary values: {inventory.values()}")
        print("Sample lookup - 'sword' in inventory:"
              f" {inventory.get('sword') is not None}")

    except ValueError as e:
        print(f"[ValueError]: {e}")
    except InventoryError as e:
        print(f"[InventoryError]: {e}")
    except Exception as e:
        print(f"[Error]: {e}")


if __name__ == "__main__":
    main()

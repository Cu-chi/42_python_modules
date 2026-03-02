from typing import Any, Literal, Callable


def mage_counter() -> Callable:
    number_called: int = 0

    def counter() -> int:
        nonlocal number_called
        number_called += 1
        return number_called
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power: int = 0

    def accumulator() -> int:
        nonlocal total_power
        total_power += initial_power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda item_name: enchantment_type + " " + item_name


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, Any] = {}

    def recall(key: str) -> Any | Literal['Memory not found']:
        value: Any = vault.get(key)
        return value if value else "Memory not found"

    def store(key: str, value: Any) -> None:
        vault.update({key: value})

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    counter: Callable = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

    print("\nTesting spell accumulator...")
    accumulator: Callable = spell_accumulator(5)
    for i in range(1, 4):
        print(f"Call {i}: {accumulator()}")

    print("\nTesting enchantment factory...")
    print(enchantment_factory("Flaming")("Sword"))
    print(enchantment_factory("Frozen")("Shield"))

    print("\nTesting memory vault...")
    vault_funcs: dict[str, Callable] = memory_vault()
    print(f"Getting unknown key 'test': {vault_funcs['recall']('test')}")
    print("Adding 'test': 42 to vault")
    vault_funcs['store']('test', 42)
    print(f"Getting known key 'test': {vault_funcs['recall']('test')}")


if __name__ == "__main__":
    main()

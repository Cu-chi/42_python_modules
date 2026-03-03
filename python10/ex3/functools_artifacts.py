import functools
import operator
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(operator.add, spells)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)
    elif operation == "max":
        return functools.reduce(max, spells)
    elif operation == "min":
        return functools.reduce(min, spells)
    raise ValueError(f"operation '{operation}' is not valid")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": functools.partial(
            base_enchantment, power=50, element="fire"),
        "ice_enchant": functools.partial(
            base_enchantment, power=50, element="ice"),
        "lightning_enchant": functools.partial(
            base_enchantment, power=50, element="lightning")
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def spell(arg: Any) -> str:
        return f"Type '{type(arg).__name__}' is unknown"

    @spell.register
    def _(damage: int) -> str:
        return f"Damage {damage}"

    @spell.register
    def _(enchantment: str) -> str:
        return f"Enchantment {enchantment}"

    @spell.register
    def _(enchantments: list) -> str:
        return f"{[spell(enchantment) for enchantment in enchantments]}"
    return spell


def main() -> None:
    spell_powers: list[int] = [15, 48, 41, 40, 38, 15]
    print("\nTesting spell reducer...")
    for op in ['add', 'multiply', 'max', 'min']:
        print(f"{op.capitalize()}: {spell_reducer(spell_powers, op)}")

    def base_enchantment(power: int, element: str, target: str) -> None:
        print(f"Target {target} has now {power} power and element {element}")

    print("\nTesting partial enchanter...")
    partials: dict[str, Callable] = partial_enchanter(base_enchantment)
    for key in ['fire_enchant', 'ice_enchant', 'lightning_enchant']:
        partials[key](target="sword")

    print("Testing memoized fibonacci...")
    for n in [10, 15, 20]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    print("\nTesting spell dispatcher...")
    spell: Callable = spell_dispatcher()
    print(spell(10))
    print(spell("fire"))
    print(spell(10.0))
    print(spell([4, 8, [50, "fire"], "ice", 0.33, 15]))


if __name__ == "__main__":
    main()

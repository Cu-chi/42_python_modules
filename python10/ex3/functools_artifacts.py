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


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> callable:
    pass


def main() -> None:
    spell_powers: list[int] = [15, 48, 41, 40, 38, 15]
    print("\nTesting spell reducer...")
    for op in ['add', 'multiply', 'max', 'min']:
        print(f"{op.capitalize()}: {spell_reducer(spell_powers, op)}")


if __name__ == "__main__":
    main()

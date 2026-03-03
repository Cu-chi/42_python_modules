from functools import wraps
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start: float = time.time()
        result: Any = func(*args, **kwargs)
        print(f"Spell completed in {time.time() - start:.2f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if args[2] >= min_power:
                return func(*args, **kwargs)
            print("Insufficient power for this spell")
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            n_attempt: int = 0
            while n_attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    n_attempt += 1
                    print("Spell failed, retrying... "
                          f"({n_attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempt"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.isprintable()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def tester_timer() -> str:
    time.sleep(0.10)
    return "Result: Fireball cast!"


def main() -> None:
    print("\nTesting spell timer...")
    result: str = tester_timer()
    print(result)

    print("\nTesting MageGuild...")
    mage_build: MageGuild = MageGuild()
    print(mage_build.validate_mage_name("Ice Wizard"))
    print(mage_build.validate_mage_name("Ice \nWizard"))
    print(mage_build.cast_spell("Lightning", 15))
    mage_build.cast_spell("Lightning", 8)

    print("\nTesting retry spell")

    @retry_spell(max_attempts=3)
    def spell_tester(fail: bool) -> str:
        if fail:
            raise Exception
        return "spell tester ok!"
    print(spell_tester(False))
    print(spell_tester(True))


if __name__ == "__main__":
    main()

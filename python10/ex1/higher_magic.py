def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args: spell1(*args) + ", " + spell2(*args)


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda: base_spell() * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *args: spell(*args) if condition(*args) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda *args: [spell(*args) for spell in spells]


def main() -> None:
    print("\nTesting spell combiner...")

    def fireball(name: str) -> str:
        return "Fireball hits " + name

    def heal(name: str) -> str:
        return "Heals " + name
    combined: callable = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon')}")

    print("\nTesting power amplifier...")
    amplified: callable = power_amplifier(lambda: 10, 3)
    print(f"Original 10, Amplified: {amplified()}")

    print("\nTesting conditional caster...")

    def condition(hp: int) -> str:
        return hp < 3

    def spell(hp: int) -> str:
        return f"Heals to {hp + 5}hp"
    conditional_spell: callable = conditional_caster(condition, spell)
    print(f"Conditional caster with hp=10: {conditional_spell(10)}")
    print(f"Conditional caster with hp=2: {conditional_spell(2)}")

    print("\nTesting spell sequence...")

    def fireball(name: str) -> str:
        return "Fireball hits " + name

    def heal(name: str) -> str:
        return "Heals " + name

    def ice(name: str) -> str:
        return "Froze " + name

    def buff(name: str) -> str:
        return "Buff " + name

    print("list of results:")
    spells: callable = spell_sequence([fireball, heal, ice, buff])
    for spell in spells("Dragon"):
        print("- " + spell)


if __name__ == "__main__":
    main()

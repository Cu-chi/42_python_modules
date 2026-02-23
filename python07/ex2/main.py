from ex0.Card import CardRarity, Card
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def get_methods(cls) -> list[str]:
    return [method for method in dir(cls)
            if callable(getattr(cls, method))
            and not method.startswith('__')]


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print(f"- Card: {get_methods(Card)}")
    print(f"- Combatable: {get_methods(Combatable)}")
    print(f"- Magical: {get_methods(Magical)}")

    elite: EliteCard = EliteCard("Arcane Warrior", 5,
                                 CardRarity.LEGENDARY.value, 3, 5, 10,
                                 "melee", 4, 4)
    print("\nPlaying Arcane Warrior (Elite Card):\n")

    print("Combat phase:")
    enemy: CreatureCard = CreatureCard("Enemy", 2, CardRarity.COMMON.value,
                                       2, 7)
    print(f"Attack result: {elite.attack(enemy)}")
    print(f"Defense result: {elite.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite.channel_mana(7)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()

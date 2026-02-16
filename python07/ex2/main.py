from ex0.Card import CardRarity
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

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

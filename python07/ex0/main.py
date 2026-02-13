from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    fire_dragon: CreatureCard = CreatureCard("Fire Dragon", 5,
                                             "Legendary", 7, 5)
    print(f"{fire_dragon.get_card_info()}")

    mana: int = 6
    print(f"\nPlaying Fire Dragon with {mana} mana available:")
    print(f"Playable: {fire_dragon.is_playable(mana)}")
    game_state: dict = {}
    game_state = fire_dragon.play(game_state)
    print(f"Play result: {game_state}")

    goblin_warrior: CreatureCard = CreatureCard("Goblin Warrior", 3,
                                                "Common", 5, 5)
    game_state = goblin_warrior.play(game_state)
    print("\nFire Dragon attacks Goblin Warrior:")
    attack_result: dict = fire_dragon.attack_target(goblin_warrior)
    print(f"Attack result: {attack_result}")

    mana = 3
    print(f"\nTesting insufficient mana ({mana} available):")
    print(f"Playable: {fire_dragon.is_playable(mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()

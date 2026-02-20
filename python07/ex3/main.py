from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    game_engine: GameEngine = GameEngine()
    game_engine.configure_engine(FantasyCardFactory, AggressiveStrategy)

    print(f"Available types: {game_engine.factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    deck: dict
    try:
        deck = game_engine.factory.create_themed_deck(3)
    except Exception as e:
        print(f"Error while creating theme deck: {e}")
        exit(1)
    print("Hand: [", end="")
    first: bool = True
    for _, card in deck.items():
        if first:
            first = False
        else:
            print(", ", end="")
        print(f"{card.name} ({card.cost})", end="")
    print("]")

    print("\nTurn execution:")
    print("Strategy: AggressiveStrategy")

    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
    print()


if __name__ == "__main__":
    main()

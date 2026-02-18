from ex3.FantasyCardFactory import FantasyCardFactory


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")
    fantasy: FantasyCardFactory = FantasyCardFactory()
    print(f"Available types: {fantasy.get_supported_types()}")

    print("Simulating aggressive turn...")
    deck: dict = fantasy.create_themed_deck(3)
    print("Hand: [", end="")
    first: bool = True
    for _, card in deck.items():
        if first:
            first = False
        else:
            print(", ", end="")
        print(f"{card.name} ({card.cost})", end="")
    print("]")

    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
    print()


if __name__ == "__main__":
    main()

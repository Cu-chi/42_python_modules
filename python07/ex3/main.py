from ex3.FantasyCardFactory import FantasyCardFactory


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")
    fantasy: FantasyCardFactory = FantasyCardFactory()
    print(f"Available types: {fantasy.get_supported_types()}")

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()

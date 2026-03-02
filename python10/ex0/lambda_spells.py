def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda mage: mage["power"] >= min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda spell: f"* {spell} *", spells)


def mage_stats(mages: list[dict]) -> dict:
    stats: dict = {
        "max_power": max(mages, key=lambda mage: mage["power"]),
        "min_power": min(mages, key=lambda mage: mage["power"]),
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages), 2),
    }
    return stats


def main() -> None:
    artifacts: list[dict] = [
        {'name': 'Wind Cloak', 'power': 82, 'type': 'relic'},
        {'name': 'Wind Cloak', 'power': 68, 'type': 'accessory'},
        {'name': 'Ice Wand', 'power': 115, 'type': 'weapon'},
        {'name': 'Lightning Rod', 'power': 89, 'type': 'accessory'}
    ]
    mages: list[dict] = [
        {'name': 'Nova', 'power': 66, 'element': 'lightning'},
        {'name': 'Casey', 'power': 70, 'element': 'fire'},
        {'name': 'Zara', 'power': 54, 'element': 'shadow'},
        {'name': 'Kai', 'power': 87, 'element': 'shadow'},
        {'name': 'Zara', 'power': 73, 'element': 'lightning'}
    ]
    spells: list[str] = ['shield', 'heal', 'earthquake', 'blizzard']
    print("\nTesting artifact sorter...")

    isFirst: bool = True
    for artifact in artifact_sorter(artifacts):
        if not isFirst:
            print(" comes before ", end="")
        else:
            isFirst = False
        print(f"{artifact['name']} ({artifact['power']} power)", end="")
    print("\n")

    print("Testing spell transformer...")
    for elem in spell_transformer(spells):
        print(elem + " ", end="")

    print("\n\nTesting power filter (with a filter at 70)...")
    for mage in power_filter(mages, 70):
        print(f"{mage['name']} ({mage['power']} power)")

    print("\nGetting mages stats...")
    stats: dict = mage_stats(mages)
    print(f"Mage with max power: {stats['max_power']['name']}"
          f" ({stats['max_power']['power']} power)")
    print(f"Mage with min power: {stats['min_power']['name']}"
          f" ({stats['min_power']['power']} power)")
    print(f"Average power: {stats['avg_power']}")


if __name__ == "__main__":
    main()

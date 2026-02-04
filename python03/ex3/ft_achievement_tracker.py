def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice_achievements: set[str] = {'first_kill', 'level_10',
                                    'treasure_hunter', 'speed_demon'}
    bob_achievements: set[str] = {'first_kill', 'level_10',
                                  'boss_slayer', 'collector'}
    charlie_achievements: set[str] = {'level_10', 'treasure_hunter',
                                      'boss_slayer', 'speed_demon',
                                      'perfectionist'}
    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")
    print("\n=== Achievement Analytics ===")
    achievements: set[str] = alice_achievements\
        .union(bob_achievements).union(charlie_achievements)
    print(f"All unique achievements: {achievements}")
    print(f"Total unique achievements: {len(achievements)}\n")
    common_to_all: set[str] = alice_achievements\
        .intersection(bob_achievements).intersection(charlie_achievements)
    print(f"Common to all players: {common_to_all}")
    rare: set[str] = set()
    for achievement in achievements:
        nb = 0
        if achievement in alice_achievements:
            nb += 1
        if achievement in bob_achievements:
            nb += 1
        if achievement in charlie_achievements:
            nb += 1
        if nb == 1:
            rare = rare.union({achievement})
    print(f"Rare achievements: {rare}\n")
    print("Alice vs Bob common: "
          f"{alice_achievements.intersection(bob_achievements)}")
    print("Alice unique: "
          f"{alice_achievements.difference(bob_achievements)}")
    print("Bob unique: "
          f"{bob_achievements.difference(alice_achievements)}")


if __name__ == "__main__":
    main()

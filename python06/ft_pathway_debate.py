def absolute_import() -> None:
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print("lead_to_gold(): " + lead_to_gold())
    print("stone_to_gem(): " + stone_to_gem())


def relative_import() -> None:
    from alchemy.transmutation.advanced import philosophers_stone, \
        elixir_of_life
    print("philosophers_stone(): " + philosophers_stone())
    print("elixir_of_life(): " + elixir_of_life())


def pck_access() -> None:
    import alchemy.transmutation
    print("alchemy.transmutation.lead_to_gold(): "
          + alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone(): "
          + alchemy.transmutation.philosophers_stone())


def main() -> None:
    print("\n=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")
    absolute_import()
    print("\nTesting Relative Imports (from advanced.py):")
    relative_import()
    print("\nTesting Package Access:")
    pck_access()
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()

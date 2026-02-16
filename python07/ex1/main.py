from ex0.CreatureCard import CreatureCard
from ex0.Card import Card, CardRarity
from ex1.SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck_manager: Deck = Deck()
    fire_dragon: CreatureCard = CreatureCard("Fire Dragon", 5,
                                             CardRarity.LEGENDARY.value, 7, 5)
    lightning_bolt: SpellCard = SpellCard("Lightning Bolt", 3,
                                          CardRarity.RARE.value,
                                          EffectType.DAMAGE.value)
    mana_crystal: ArtifactCard = ArtifactCard("Mana Crystal", 4,
                                              CardRarity.UNCOMMON.value, 5,
                                              "Permanent: +1 mana per turn'")
    deck_manager.add_card(fire_dragon)
    deck_manager.add_card(mana_crystal)
    deck_manager.add_card(lightning_bolt)
    print(f"Deck stats: {deck_manager.get_deck_stats()}")
    print("\nDrawing and playing cards:\n")

    game_state: dict = {}
    for _ in range(3):
        card: Card = deck_manager.draw_card()
        print(f"Drew: {card.name} ({card.type})")
        game_state = card.play(game_state)
        print(f"Play result: {game_state}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()

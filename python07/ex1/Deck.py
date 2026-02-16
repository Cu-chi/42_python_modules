from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card: Card) -> bool:
        try:
            self.cards.remove(card)
        except Exception:
            return False
        return True

    def suffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        nb_cards: int = len(self.cards)
        if nb_cards == 0:
            return {
                "total_cards": 0, "creatures": 0,
                "artifacts": 0, "spells": 0, "avg_cost": 0.0
            }
        return {
            "total_cards": nb_cards,
            "creatures": sum([1 for c in self.cards if c.type == "Creature"]),
            "artifacts": sum([1 for c in self.cards if c.type == "Artifact"]),
            "spells": sum([1 for c in self.cards if c.type == "Spell"]),
            "avg_cost": sum([c.cost for c in self.cards]) / nb_cards
        }

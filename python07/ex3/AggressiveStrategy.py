from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.strategy = "AggressiveStrategy"

    @staticmethod
    def sort_attack(hand: list) -> list[CreatureCard]:
        return sorted([
            card for card in hand
            if isinstance(card, CreatureCard)
        ], key=lambda card: -card.attack)

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        turn: dict = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0
        }
        best_attack: list[CreatureCard] = self.sort_attack(hand)
        for card in best_attack:
            hand.remove(card)
        priorized: list = self.prioritize_targets(battlefield)
        for creature in priorized:
            card: Card
            if len(best_attack) > 0:
                card = best_attack[0]
                attack: dict = card.attack_target(creature)
                turn["damage_dealt"] += attack["damage_dealt"]

            else:
                for _card in hand:
                    if isinstance(_card, SpellCard):
                        if _card.effect_type == "damage":
                            card = _card
                            card.resolve_effect(battlefield)
                            turn["damage_dealt"] += _card.cost \
                                * len(battlefield)
                    hand.pop(0)
            turn["mana_used"] += card.cost
            turn["cards_played"].append(card.name)
        return turn

    def get_strategy_name(self) -> str:
        return self.strategy

    def prioritize_targets(self, available_targets: list) -> list:
        return [card for card in available_targets
                if isinstance(card, CreatureCard)]

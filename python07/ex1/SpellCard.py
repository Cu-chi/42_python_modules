from ex0.Card import Card
from enum import Enum


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        """Initialize a CreatureCard object

        Args:
            name (str): name of the card
            cost (int): cost of the card, must be positive and not 0
            rarity (str): rarity (Common,
            Uncommon, Rare, Legendary)
            effect_type (int): effect type "damage", "heal",
            "buff", "debuff"

        Raises:
            ValueError: if effect_type is not valid
        """
        super().__init__(name, cost, rarity)
        self.effect_type: str = ""
        for effect in EffectType:
            if effect_type == effect.value:
                self.effect_type: str = effect_type
        if self.effect_type == "":
            raise ValueError(f"effect_type '{effect_type}' is invalid")
        self.type: str = "Spell"
        self.consumed: bool = False

    def get_card_info(self) -> dict:
        infos: dict = super().get_card_info()
        infos.update({
            "effect_type": self.effect_type
        })
        return infos

    def play(self, game_state: dict) -> dict:
        game_state.update({
            "card_played": self.name,
            "mana_used": self.cost
        })
        if self.effect_type == EffectType.DAMAGE.value:
            game_state.update({
                "effect": f"Deal {self.cost} damage to target"
            })
        elif self.effect_type == EffectType.BUFF.value:
            game_state.update({
                "effect": f"Increase target attack +{self.cost}"
            })
        elif self.effect_type == EffectType.DEBUFF.value:
            game_state.update({
                "effect": f"Decrease target attack -{self.cost}"
            })
        elif self.effect_type == EffectType.HEAL.value:
            game_state.update({
                "effect": f"Heal target by {self.cost}hp"
            })
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        if not self.consumed:
            for target in targets:
                if self.effect_type == EffectType.DAMAGE.value:
                    target.health -= self.cost
                elif self.effect_type == EffectType.BUFF.value:
                    target.attack += self.cost
                elif self.effect_type == EffectType.DEBUFF.value:
                    target.attack -= self.cost
                elif self.effect_type == EffectType.HEAL.value:
                    target.health += self.cost
            self.consumed = True
        return {
            "effect_type": self.effect_type,
            "targets": targets,
            "consumed": self.consumed
        }

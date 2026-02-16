from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 shield: int, attack: int, health: int,
                 combat_type: str, spell_cast: int,
                 attack_mana: int) -> None:
        super().__init__(name, cost, rarity)
        if shield <= 0:
            raise ValueError("'shield' attribute must be positive")
        self.shield: int = shield
        if attack <= 0:
            raise ValueError("'attack' attribute must be positive")
        self._attack: int = attack
        if health <= 0:
            raise ValueError("'health' attribute must be positive")
        self.health: int = health
        self.combat_type: str = combat_type
        self.spell_cast: int = spell_cast
        self.attack_mana: str = attack_mana

    def play(self, game_state: dict) -> dict:
        game_state.update({
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.type} summoned to battlefield"
        })
        return game_state

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self._attack,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken: int = incoming_damage - self.shield
        if damage_taken < 0:
            damage_taken = 0
        damage_blocked: int = incoming_damage - damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": (self.health - damage_taken) > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "damage": self._attack,
            "combat_type": self.combat_type,
            "defense": self.shield,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.spell_cast
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            "channeled": 3,
            "total_mana": amount
        }

    def get_magic_stats(self) -> dict:
        return {
            "cost": self.spell_cast
        }

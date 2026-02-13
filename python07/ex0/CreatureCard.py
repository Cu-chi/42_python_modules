from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        """Initialize a CreatureCard object

        Args:
            name (str): name of the card
            cost (int): cost of the card, must be positive and not 0
            rarity (str): rarity (Common,
            Uncommon, Rare, Legendary)
            attack (int): attack damage, must be positive and not 0
            health (int): health, must be positive and not 0

        Raises:
            ValueError: if attack is equal or less than 0
            ValueError: if health is equal or less than 0
        """
        super().__init__(name, cost, rarity)
        if attack > 0:
            self.attack: int = attack
        else:
            raise ValueError("'attack' attribute must be positive")
        if health > 0:
            self.health: int = health
        else:
            raise ValueError("'health' attribute must be positive")
        self.type = "Creature"

    def get_card_info(self) -> dict:
        infos: dict = super().get_card_info()
        infos.update({
            "attack": self.attack,
            "health": self.health
        })
        return infos

    def play(self, game_state: dict) -> dict:
        game_state.update({
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.type} summoned to battlefield"
        })
        return game_state

    def attack_target(self, target: 'CreatureCard') -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": self.attack >= target.health
        }

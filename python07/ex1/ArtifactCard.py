from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        """Initialize a CreatureCard object

        Args:
            name (str): name of the card
            cost (int): cost of the card, must be positive and not 0
            rarity (str): rarity (Common,
            Uncommon, Rare, Legendary)
            durability (int): durability of the artifact
            effect (str): effect of the artifact

        Raises:
            ValueError: if durability is less or equal to 0
            ValueError: if effect is empty
        """
        super().__init__(name, cost, rarity)
        self.type: str = "Artifact"
        if durability <= 0:
            raise ValueError("durability must be greater than 0")
        self.durability: int = durability
        if effect == "":
            raise ValueError("effect can't be empty")
        self.effect: str = effect
        self.active: bool = False

    def get_card_info(self) -> dict:
        infos: dict = super().get_card_info()
        infos.update({
            "effect": self.effect,
            "durability": self.durability,
            "active": self.active
        })
        return infos

    def play(self, game_state: dict) -> dict:
        game_state.update({
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        })
        return game_state

    def activate_ability(self) -> dict:
        state: bool = self.active
        self.active = True
        return {
            "effect": self.effect,
            "durability": self.durability,
            "already_used": state
        }

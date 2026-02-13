from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack > 0:
            self.attack: int = attack
        else:
            raise ValueError("'attack' attribute must be positive")
        if health > 0:
            self.health: int = health
        else:
            raise ValueError("'health' attribute must be positive")

    def get_card_info(self) -> dict:
        infos: dict = super().get_card_info()
        infos.update({
            "attack": self.attack,
            "health": self.health
        })
        return infos

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        pass

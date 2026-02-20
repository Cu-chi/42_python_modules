from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.turns: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0
        self.battlefield: list = []
        self.hand: list = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory: CardFactory = factory()
        print(f"Factory: {type(self.factory).__name__}")
        self.strategy: GameStrategy = strategy()
        print(f"Strategy: {self.strategy.get_strategy_name()}")

    def simulate_turn(self) -> dict:
        self.turns += 1
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        if len(self.hand) == 0:
            self.hand = self.factory.create_themed_deck(3)
        turn_res: dict = self.strategy.execute_turn(self.hand,
                                                    self.battlefield)
        self.total_damage += turn_res["damage_dealt"]
        return turn_res

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": type(self.strategy).__name__,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        print(f"Factory: {factory.__qualname__}")
        self.factory: CardFactory = factory()
        print(f"Factory: {type(self.factory).__name__}")
        self.strategy: GameStrategy = strategy()
        print(f"Strategy: {self.strategy.get_strategy_name()}")

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        pass

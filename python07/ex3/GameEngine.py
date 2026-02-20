from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        print(f"Factory: {factory.__qualname__}")
        self.factory: CardFactory = factory()
        print(f"Strategy: {strategy.__qualname__}")
        self.strategy: GameStrategy = strategy()

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        pass

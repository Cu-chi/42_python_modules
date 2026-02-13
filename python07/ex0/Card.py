from abc import ABC, abstractmethod
from enum import Enum


class CardRarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if name == "":
            raise ValueError("Card name cannot be empty")
        self.name: str = name
        if cost < 0:
            raise ValueError("Card cost cannot be negative")
        self.cost: int = cost
        self.rarity: str = ""
        for card_rarity in CardRarity:
            if rarity == card_rarity.value:
                self.rarity: str = rarity
        if self.rarity == "":
            raise ValueError(f"rarity '{rarity}' is invalid")

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

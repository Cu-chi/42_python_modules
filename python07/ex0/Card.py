from abc import ABC, abstractmethod
from enum import Enum


class CardRarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize a Card object

        Args:
            name (str): Name of the Card
            cost (int): Cost of the card (>= 0)
            rarity (str): Rarity of the Card (Common,
            Uncommon, Rare, Legendary)

        Raises:
            ValueError: if name is empty
            ValueError: if cost is negative
            ValueError: if rarity is invalid
        """
        if name == "":
            raise ValueError("Card name cannot be empty")
        self.name: str = name
        if cost < 0:
            raise ValueError("Card cost cannot be negative")
        self.cost: int = cost
        self.rarity: str = ""
        for card_rarity in CardRarity:
            if rarity == card_rarity.value:
                self.rarity = rarity
        if self.rarity == "":
            raise ValueError(f"rarity '{rarity}' is invalid")
        self.type: str = "Unknown"

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.type
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

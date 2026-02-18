from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import Any
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.__creatures: dict[str, dict] = {
            "dragon": {
                "name": "Fire Dragon",
                "cost": 5,
                "rarity": "Legendary",
                "attack": 7,
                "health": 5
            },
            "goblin": {
                "name": "Goblin Warrior",
                "cost": 2,
                "rarity": "Common",
                "attack": 2,
                "health": 1
            }
        }
        self.__spells: dict[str, dict] = {
            "fireball": {
                "name": "Fireball",
                "cost": 4,
                "rarity": "Uncommon",
                "effect_type": "damage"
            }
        }
        self.__artifacts: dict[str, dict] = {
            "mana_ring": {
                "name": "Mana Crystal",
                "cost": 2,
                "rarity": "Common",
                "durability": 5,
                "effect": "Permanent: +1 mana per turn"
            }
        }

        self.__supported_types: list = [
            "creatures",
            "spells",
            "artifacts"
        ]

    @staticmethod
    def get_power(card: list[dict[str, Any]], card_type: str) -> int:
        if card_type == "creature":
            return card["health"] + card["attack"] - card["cost"]
        elif card_type == "spell":
            return 5 - card["cost"]
        elif card_type == "artifact":
            return card["durability"] - card["cost"]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for creature_name, creature_data in self.__creatures.items():
                if creature_name == name_or_power:
                    return CreatureCard(creature_data["name"],
                                        creature_data["cost"],
                                        creature_data["rarity"],
                                        creature_data["attack"],
                                        creature_data["health"])
        elif isinstance(name_or_power, int):
            for _, creature_data in self.__creatures.items():
                if self.get_power(creature_data, "creature") == name_or_power:
                    return CreatureCard(creature_data["name"],
                                        creature_data["cost"],
                                        creature_data["rarity"],
                                        creature_data["attack"],
                                        creature_data["health"])
        else:
            return CreatureCard(self.__creatures[0]["name"],
                                self.__creatures[0]["cost"],
                                self.__creatures[0]["rarity"],
                                self.__creatures[0]["attack"],
                                self.__creatures[0]["health"])

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for spell_name, spell_data in self.__spells.items():
                if spell_name == name_or_power:
                    return SpellCard(spell_data["name"],
                                     spell_data["cost"],
                                     spell_data["rarity"],
                                     spell_data["effect_type"])
        elif isinstance(name_or_power, int):
            for _, spell_data in self.__spells.items():
                if self.get_power(spell_data, "spell") == name_or_power:
                    return SpellCard(spell_data["name"],
                                     spell_data["cost"],
                                     spell_data["rarity"],
                                     spell_data["effect_type"])
        else:
            return SpellCard(self.__spells[0]["name"],
                             self.__spells[0]["cost"],
                             self.__spells[0]["rarity"],
                             self.__spells[0]["effect_type"])

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for artifact_name, artifact_data in self.__artifacts.items():
                if artifact_name == name_or_power:
                    return ArtifactCard(artifact_data["name"],
                                        artifact_data["cost"],
                                        artifact_data["rarity"],
                                        artifact_data["durability"],
                                        artifact_data["effect"])
        elif isinstance(name_or_power, int):
            for _, artifact_data in self.__artifacts.items():
                if self.get_power(artifact_data, "artifact") == name_or_power:
                    return ArtifactCard(artifact_data["name"],
                                        artifact_data["cost"],
                                        artifact_data["rarity"],
                                        artifact_data["durability"],
                                        artifact_data["effect"])
        else:
            return ArtifactCard(self.__artifacts[0]["name"],
                                self.__artifacts[0]["cost"],
                                self.__artifacts[0]["rarity"],
                                self.__artifacts[0]["durability"],
                                self.__artifacts[0]["effect"])

    def create_themed_deck(self, size: int) -> dict:
        if size <= 0:
            return {}
        themed_deck: dict = {}
        for _ in range(size):
            random_type: str = self.__supported_types[
                random.randint(0, len(self.__supported_types) - 1)]
            if random_type == "creatures":
                keys: list = list(self.__creatures.keys())
                random_card_name: str = keys[random.randint(0, len(keys) - 1)]
                themed_deck.update({random_card_name:
                                    self.create_creature(random_card_name)})
            elif random_type == "spells":
                keys: list = list(self.__spells.keys())
                random_card_name: str = keys[random.randint(0, len(keys) - 1)]
                themed_deck.update({random_card_name:
                                    self.create_spell(random_card_name)})
            elif random_type == "artifacts":
                keys: list = list(self.__artifacts.keys())
                random_card_name: str = keys[random.randint(0, len(keys) - 1)]
                themed_deck.update({random_card_name:
                                    self.create_artifact(random_card_name)})
        return themed_deck

    def get_supported_types(self) -> dict:
        return {
            name: list(getattr(self, f"_FantasyCardFactory__{name}").keys())
            for name in self.__supported_types
        }

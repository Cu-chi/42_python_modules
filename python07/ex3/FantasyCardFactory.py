from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import Any


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.__creatures: list[str] = ["dragon", "goblin"]
        self.__spells: list[str] = ["fireball"]
        self.__artifacts: list[str] = ["mana_ring"]

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
            for creature in self.__creatures:
                if creature["name"] == name_or_power:
                    return CreatureCard(creature["name"],
                                        creature["cost"],
                                        creature["rarity"],
                                        creature["attack"],
                                        creature["health"])
        elif isinstance(name_or_power, int):
            for creature in self.__creatures:
                if self.get_power(creature, "creature") == name_or_power:
                    return CreatureCard(creature["name"],
                                        creature["cost"],
                                        creature["rarity"],
                                        creature["attack"],
                                        creature["health"])
        else:
            return CreatureCard(self.__creatures[0]["name"],
                                self.__creatures[0]["cost"],
                                self.__creatures[0]["rarity"],
                                self.__creatures[0]["attack"],
                                self.__creatures[0]["health"])

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for spell in self.__spells:
                if spell["name"] == name_or_power:
                    return SpellCard(spell["name"],
                                     spell["cost"],
                                     spell["cost"],
                                     spell["effect_type"])
        elif isinstance(name_or_power, int):
            for spell in self.__spells:
                if self.get_power(spell, "spell") == name_or_power:
                    return SpellCard(spell["name"],
                                     spell["cost"],
                                     spell["cost"],
                                     spell["effect_type"])
        else:
            return SpellCard(self.__spells[0]["name"],
                             self.__spells[0]["cost"],
                             self.__spells[0]["cost"],
                             self.__spells[0]["effect_type"])

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for artifact in self.__artifacts:
                if artifact["name"] == name_or_power:
                    return ArtifactCard(artifact["name"],
                                        artifact["cost"],
                                        artifact["rarity"],
                                        artifact["durability"],
                                        artifact["effect"])
        elif isinstance(name_or_power, int):
            for artifact in self.__artifacts:
                if self.get_power(artifact, "artifact") == name_or_power:
                    return ArtifactCard(artifact["name"],
                                        artifact["cost"],
                                        artifact["rarity"],
                                        artifact["durability"],
                                        artifact["effect"])
        else:
            return ArtifactCard(self.__artifacts[0]["name"],
                                self.__artifacts[0]["cost"],
                                self.__artifacts[0]["rarity"],
                                self.__artifacts[0]["durability"],
                                self.__artifacts[0]["effect"])

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        return {name: self["__"+name]
                for name in self.__supported_types}

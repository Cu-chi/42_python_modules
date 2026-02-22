from ex4.TournamentCard import TournamentCard, TournamentCardAlreadyExists


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: list[TournamentCard] = []

    def register_card(self, card: TournamentCard) -> str:
        for _card in self.cards:
            if _card.id == card.id:
                raise TournamentCardAlreadyExists(f"id '{card.id}' is already"
                                                  " registered")
        self.cards.append(card)
        result: str = f"{card.name} (ID: {card.id}):\n"

        result += "- Interfaces: ["
        for base in card.__class__.__bases__:
            result += base.__name__ + ", "
        result = result[:-2] + "]\n"
        result += f"- Rating: {card.rating}\n"
        result += f"- Record: {card.wins}/{card.losses}\n"
        return result

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        return sorted(self.cards, key=lambda card: card.rating, reverse=True)

    def generate_tournament_report(self) -> dict:
        pass

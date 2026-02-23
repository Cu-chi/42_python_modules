from ex4.TournamentCard import TournamentCard, TournamentCardAlreadyExists


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: list[TournamentCard] = []
        self.match_played: int = 0

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
        result += f"- Record: {card.wins}-{card.losses}\n"
        return result

    def get_card_by_id(self, id: str) -> TournamentCard:
        for card in self.cards:
            if card.id == id:
                return card
        raise ValueError(f"id '{id}' not found")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.match_played += 1
        card1: TournamentCard = self.get_card_by_id(card1_id)
        card2: TournamentCard = self.get_card_by_id(card2_id)
        winner: TournamentCard
        loser: TournamentCard
        while card1.hp > 0 and card2.hp > 0:
            attack1: dict = card1.attack(card2)
            if attack1["dead"]:
                winner = card1
                loser = card2
            attack2: dict = card2.attack(card1)
            if attack2["dead"]:
                winner = card2
                loser = card1
        winner.update_wins(winner.wins + 1)
        loser.update_losses(loser.losses + 1)
        return {
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list:
        return sorted(self.cards, key=lambda card: card.rating, reverse=True)

    def generate_tournament_report(self) -> dict:
        total_cards: int = len(self.cards)
        if total_cards == 0:
            return {
                "total_cards": 0,
                "match_played": self.match_played,
                "avg_rating": 0,
                "plateform_status": "inactive"
            }
        return {
            "total_cards": total_cards,
            "match_played": self.match_played,
            "avg_rating": int(sum([card.rating
                                   for card in self.cards]) / total_cards),
            "plateform_status": "active"
        }

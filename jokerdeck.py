from carddeck import CardDeck
from card import Card

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for i in range(2):
            joker = Card('*** JOKER ***', i)
            self._cards.append(joker)

if __name__ == "__main__":
    j = JokerDeck("Albert")
    j.shuffle()
    print(j)
    print(j.cards)
    print()
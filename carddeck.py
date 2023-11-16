import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    def __init__(self, dealer):
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if len(self._cards) == 0:
            raise ValueError("out of cards")
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):
        return self._dealer
    
    @dealer.setter
    def dealer(self, value):
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer name must be a string")

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}/{self.dealer}"
        
if __name__ == "__main__":
    d1 = CardDeck("Django")
    print(d1)
    print(d1.dealer)

    d1.dealer = "Jerry"
    print(f"d1.dealer: {d1.dealer}")
    d1.shuffle()
    print(f"d1.cards: {d1.cards}\n")
    print(f"len(d1): {len(d1)}")
    
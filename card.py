
class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c = Card('2', 'Clubs')
    print(f"c: {c}")
    print(f"type(c): {type(c)}")
    print(f"c.rank: {c.rank}")
    print(f"repr(c): {repr(c)}")
    
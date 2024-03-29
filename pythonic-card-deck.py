import collections
card = collections.namedtuple('card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]  
      

deck = FrenchDeck()
print("Playing cards: ", len(deck))  
print(deck[12])    
        
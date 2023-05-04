class CardDeck:
    deck_of_cards = ['Ace clubs', '2 clubs', '3 clubs', '4 clubs', '5 clubs', '6 clubs', '7 clubs', '8 clubs',
                     '9 clubs', '10 clubs', 'Jack clubs', 'Queen clubs', 'King clubs',
                     'Ace diamonds', '2 diamonds', '3 diamonds', '4 diamonds', '5 diamonds', '6 diamonds', '7 diamonds',
                     '8 diamonds', '9 diamonds', '10 diamonds', 'Jack diamonds', 'Queen diamonds', 'King diamonds',
                     'Ace hearts', '2 hearts', '3 hearts', '4 hearts', '5 hearts', '6 hearts', '7 hearts', '8 hearts',
                     '9 hearts', '10 hearts', 'Jack hearts', 'Queen hearts', 'King hearts',
                     'Ace spades', '2 spades', '3 spades', '4 spades', '5 spades', '6 spades', '7 spades', '8 spades',
                     '9 spades', '10 spades', 'Jack spades', 'Queen spades', 'King spades']

    def __iter__(self):
        self.index_ = 0
        return self

    def __next__(self):
        if self.index_ <= len(self.deck_of_cards) - 1:
            x = self.deck_of_cards[self.index_]
            self.index_ += 1
            return x
        raise StopIteration


cards = CardDeck()
for i in cards:
    print(i)

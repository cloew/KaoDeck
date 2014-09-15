from kao_deck.deck import Deck

class DeckWithDiscardPile(Deck):
    """ Represents a Deck with a discard pile """
    
    def __init__(self, items=None, deck_initializer=None, reshuffle=False):
        """ Initialize the Deck With a Discard Pile """
        Deck.__init__(self, items, deck_initializer)
        self.__discard_pile__ = Deck()
        self.__reshuffle__ = reshuffle
        
    def drawFromDiscardPile(self, count=1):
        """ Draw from the discard Pile """
        return self.__discard_pile__.draw(count)
        
    def discard(self, item):
        """ Discard the given item """
        self.discardAll([item])
        
    def discardAll(self, items):
        """ Discard the given items """
        self.__discard_pile__.add(items)
        
    def peekAtDiscardPile(self):
        """ Return the card on top of the discard pile """
        return self.__discard_pile__.peek()
            
    def shuffleInDiscardPile(self):
        """ Shuffle the contents of the discard pile onto the deck """
        cards = self.drawFromDiscardPile(count=len(self.__discard_pile__))
        self.add(cards)
        self.shuffle()
        
    @property
    def discardPile(self):
        """ Return the Deck's Discard Pile """
        return self.__discard_pile__
        
    def __draw_one__(self, contents):
        """ Draws a single item """
        if self.__reshuffle__ and not self.hasContents():
            if self.__reshuffle__:
                self.shuffleInDiscardPile()
            return Deck.__draw_one__(self, contents)
        else:
            return Deck.__draw_one__(self, contents)
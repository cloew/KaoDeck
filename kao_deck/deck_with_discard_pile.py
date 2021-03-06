from .deck import Deck

class DeckWithDiscardPile(Deck):
    """ Represents a Deck with a discard pile """
    
    def __init__(self, items=None, deck_initializer=None, reshuffle=False, onReshuffle=None):
        """ Initialize the Deck With a Discard Pile """
        Deck.__init__(self, items, deck_initializer)
        self.__discard_pile__ = Deck()
        self.__reshuffle__ = reshuffle
        self.onReshuffle = onReshuffle
        
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
        """ Shuffle the contents of the discard pile onto the bottom of the deck """
        self.__discard_pile__.shuffle()
        cards = self.drawFromDiscardPile(count=len(self.__discard_pile__))
        self.__contents__[0:0] = cards
        # for card in cards:
            # self.putOnBottom(card)
        
    @property
    def discardPile(self):
        """ Return the Deck's Discard Pile """
        return self.__discard_pile__
        
    def __draw_one__(self, contents):
        """ Draws a single item """
        self.checkReshuffle()
        return Deck.__draw_one__(self, contents)
        
    def availableLength(self):
        """ Returns the length of the Deck and Discard Pile """
        length = len(self)
        if self.__reshuffle__:
            length += len(self.__discard_pile__)
        return length
        
    def __getitem__(self, index):
        """ Return the item at the given index from the top of the deck """
        requiredLength = 1
        if hasattr(index, "stop"):
            requiredLength = index.stop
        self.checkReshuffle(requiredLength=requiredLength)
        
        return Deck.__getitem__(self, index)
        
    def checkReshuffle(self, requiredLength=1):
        """ Check if you need to reshuffle the deck """
        if self.__reshuffle__ and len(self) < requiredLength:
            self.shuffleInDiscardPile()
            if self.onReshuffle:
                self.onReshuffle()
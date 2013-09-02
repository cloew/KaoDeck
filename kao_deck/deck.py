from random import shuffle

class Deck:
    """ Represents any deck of items """
    
    def __init__(self, items=None, deck_initializer=None, reshuffle=False):
        """ Initialize the Deck """
        if items is not None:
            self.__contents__ = items
        elif deck_initializer is not None:
            self.__contents__ = deck_initializer.contents
        else:
            raise TypeError("No Item List or Deck Initializer provided")
        self.__discard_pile__ = []
        self.__reshuffle__ = reshuffle
      
    def draw(self, count=1):
        """ Returns a list of items removed from the top of the deck """
        return self.__draw__(self.__contents__, count)
        
    def drawFromDiscardPile(self, count=1):
        """ Draw from the discard Pile """
        return self.__draw__(self.__discard_pile__, count)
        
    def discard(self, item):
        """ Discard the given item """
        self.__discard_pile__.append(item)
        
    def shuffle(self):
        """ Shuffle the deck """
        shuffle(self.__contents__)
        
    def topOfDiscardPile(self):
        """ Return the card on top of the discard pile """
        if len(self.__discard_pile__) > 0:
            return self.__discard_pile__[-1]
        else:
            return None
            
    def shuffleInDiscardPile(self):
        """ Shuffle the contents of the discard pile onto the deck """
        cards = self.drawFromDiscardPile(count=len(self.__discard_pile__))
        self.__contents__ += cards
        self.shuffle()
        
    def __draw__(self, contents, count):
        """ Draw count items """
        items = []
        for i in range(count):
            item = self.__draw_one__(contents)
            if item is not None:
                items.append(item)
        return items
        
    def __draw_one__(self, contents):
        """ Draws a single item """
        if len(contents) == 0:
            if self.__reshuffle__:
                self.shuffleInDiscardPile()
            if len(contents) != 0:
                return contents.pop()
            return None
        return contents.pop()
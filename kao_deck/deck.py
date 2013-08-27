from random import shuffle

class Deck:
    """ Represents any deck of items """
    
    def __init__(self, items=None, deck_initializer=None):
        """ Initialize the Deck """
        if items is not None:
            self.__contents__ = items
        elif deck_initializer is not None:
            self.__contents__ = deck_initializer.contents
        else:
            raise TypeError("No Item List or Deck Initializer provided")
        self.__discard_pile__ = []
      
    def draw(self, count=1):
        """ Returns a list of items removed from the top of the deck """
        items = []
        for i in range(count):
            item = self.__draw_one__()
            if item is not None:
                items.append(item)
        return items
        
    def discard(self, item):
        """ Discard the given item """
        self.__discard_pile__.append(item)
        
    def shuffle(self):
        """ Shuffle the deck """
        shuffle(self.__contents__)
        
    def topOfDiscardPile(self):
        """ Return the card on top of the discard pile """
        return self.__discard_pile__[-1]
        
    def __draw_one__(self):
        """ Draws a single item """
        if len(self.__contents__) == 0:
            return None
        return self.__contents__.pop()
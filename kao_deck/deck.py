from random import shuffle

class Deck:
    """ Represents any deck of items """
    
    def __init__(self, items=None, deck_initializer=None):
        """ Initialize the Deck """
        if items is not None:
            self.__contents__ = items
        elif deck_initializer is not None:
            self.__contents__ = deck_initializer.contents()
        else:
            raise TypeError("No Item List or Deck Initializer provided")
        self.__disitem_pile__ = []
      
    def draw(self, count=1):
        """ Returns a list of items removed from the top of the deck """
        items = []
        for i in range(count):
            item = self.__draw_one__()
            if item is not None:
                items.append(item)
        return items
        
    def shuffle(self):
        """ Shuffle the deck """
        shuffle(self.__contents__)
        
    def __draw_one__(self):
        """ Draws a single item """
        if len(self.deck) == 0:
            return None
        return self.deck.pop()
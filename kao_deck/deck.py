
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
        self.__discard_pile__ = []
      
    def draw(self, count=1):
        """ Returns a list of cards removed from the top of the deck """
        cards = []
        for i in range(count):
            card = self.__draw_one__()
            if card is not None:
                cards.append(card)
        return cards
        
    def __draw_one__(self):
        """ Draws a single card """
        if len(self.deck) == 0:
            return None
        return self.deck.pop()

class Deck:
    """ Represents any deck of items """
    
    def __init__(self, items):
        """ Initialize the Deck """
        self.__contents__ = items
        self.__discard_pile__ = []
      
    
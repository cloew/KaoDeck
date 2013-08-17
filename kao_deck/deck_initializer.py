from copy import deepcopy

class DeckInitializer:
    """ A Helper class to initialize a deck with a set of cards """
    
    def __init__(self):
        """ Initialize the Deck Initializer """
        self.__items__ = []
    
    def addSameItem(self, item, count):
        """ Adds count copies of the given item.
            This method creates count-1 deep copied versions of the given item """
        self.__items__.append(item)
        for i in range(count-1):
            copy = deepcopy(item)
            self.__items__.append(copy)
        
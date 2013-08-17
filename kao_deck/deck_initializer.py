from copy import deepcopy

class DeckInitializer:
    """ A Helper class to initialize a deck with a set of cards """
    
    def __init__(self):
        """ Initialize the Deck Initializer """
        self.__contents__ = []
    
    def addSameItem(self, item, count):
        """ Adds count copies of the given item.
            This method creates count-1 deep copied versions of the given item """
        self.__contents__.append(item)
        for i in range(count-1):
            copy = deepcopy(item)
            self.__contents__.append(copy)
        
    @property
    def contents(self):
        """ Return the Deck Initializers Contents """
        return __contents__
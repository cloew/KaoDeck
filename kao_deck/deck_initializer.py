from copy import deepcopy

class Entry:
    """ Represents an entry in the Deck Initializer """
    
    def __init__(self, item, count=1):
        """ Initialize the entry """
        self.item = item
        self.count = count
        
    def generateContents(self):
        """ Generate the contents for the new deck """
        contents = []
        for i in range(self.count):
            copy = deepcopy(self.item)
            contents.append(copy)
        return contents

class DeckInitializer:
    """ A Helper class to initialize a deck with a set of cards """
    
    def __init__(self):
        """ Initialize the Deck Initializer """
        self.__entries__ = []
    
    def addItem(self, item, count=1):
        """ Adds count copies of the given item.
            This method creates count-1 deep copied versions of the given item """
        entry = Entry(item, count=count)
        self.__entries__.append(entry)
        
    def generateContents(self):
        """ Generate the contents for the new deck """
        contents = []
        for entry in self.__entries__:
            contents += entry.generateContents()
        return contents
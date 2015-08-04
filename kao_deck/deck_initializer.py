import copy

class Entry:
    """ Represents an entry in the Deck Initializer """
    
    def __init__(self, item, count=1, deep=True):
        """ Initialize the entry """
        self.item = item
        self.count = count
        self.deep = deep
        
    def generateContents(self):
        """ Generate the contents for the new deck """
        contents = []
        for i in range(self.count):
            if self.deep:
                copiedItem = copy.deepcopy(self.item)
            else:
                copiedItem = copy.copy(self.item)
            contents.append(copiedItem)
        return contents

class DeckInitializer:
    """ A Helper class to initialize a deck with a set of cards """
    
    def __init__(self):
        """ Initialize the Deck Initializer """
        self.__entries__ = []
    
    def addItem(self, item, count=1, deep=True):
        """ Adds count copies of the given item.
            This method creates count-1 copied versions of the given item """
        entry = Entry(item, count=count, deep=deep)
        self.__entries__.append(entry)
        
    def generateContents(self):
        """ Generate the contents for the new deck """
        contents = []
        for entry in self.__entries__:
            contents += entry.generateContents()
        return contents
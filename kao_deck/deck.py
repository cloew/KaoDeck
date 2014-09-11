from random import shuffle

class Deck:
    """ Represents any deck of items """
    
    def __init__(self, items=None, deck_initializer=None):
        """ Initialize the Deck """
        if items is not None:
            self.__contents__ = items
        elif deck_initializer is not None:
            self.__contents__ = deck_initializer.generateContents()
        else:
            raise TypeError("No Item List or Deck Initializer provided")
      
    def draw(self, count=1):
        """ Returns a list of items removed from the top of the deck """
        return self.__draw__(self.__contents__, count)
        
    def add(self, items):
        """ Add the items to the Deck """
        for item in items:
            self.__contents__.append(item)
            
    def remove(self, item):
        """ Remove a item from the deck """
        self.__contents__.remove(item)
        
    def peek(self):
        """ Peek at the top item of the deck """
        if self.hasContents():
            return self.__contents__[-1]
        return None
        
    def shuffle(self):
        """ Shuffle the deck """
        shuffle(self.__contents__)
        
    def hasContents(self):
        """ Returns if the deck has contents """
        return len(self) > 0
        
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
        if self.hasContents():
            return contents.pop()
        return None
        
    def __len__(self):
        """ Returns the length of the Deck """
        return len(self.__contents__)
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.__contents__[index]
        
    def __iter__(self):
        """ Return the Deck Iterator """
        return self.__contents__.__iter__()
import random

class State():
    def __init__(self, playerSquares, oppSquares):
        self.__playerSquares = playerSquares
        self.__oppSquares = oppSquares
        self.__heuristic = self.genHeuristic()
        
    #returns the coordinates of all squares currently held by the player in the form of a list of two element lists
    def getPlayerSquares(self):
        return self.__playerSquares
    
    #Appends the list of opponent squares based on passed coordinate
    #If the coordinate is already held by one player, False is returned. Else, True.
    def addPlayerSquare(self, coordinate):
        if((coordinate not in self.__playerSquares) and (coordinate not in self.__oppSquares)):
            self.__playerSquares.append(coordinate)
            return True
        else:
            return False
        
    #returns the coordinates of all squares currently held by the opponent in the form of a list of two element lists
    def getOppSquares(self):
        return self.__oppSquares
    
    #Appends the list of opponent squares based on passed coordinate
    #If the coordinate is already held by one player, False is returned. Else, True.
    def addOppSquare(self, coordinate):
        if((coordinate not in self.__playerSquares) and (coordinate not in self.__oppSquares)):
            self.__oppSquares.append(coordinate)
            return True
        else:
            return False
    def getHeuristic(self):
        return self.__heuristic
    def genHeuristic(self):
        return random.randint(1, 50)
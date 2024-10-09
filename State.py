class State():
    def __init__(self, playerSquares, oppSquares):
        self.__playerSquares = playerSquares
        self.__oppSquares = oppSquares

    def getPlayerSquares(self):
        return self.__playerSquares
    def addPlayerSquare(self, coordinate):
        if((coordinate not in self.__playerSquares) and (coordinate not in self.__oppSquares)):
            self.__playerSquares.append(coordinate)
            return True
        else:
            return False
    def getOppSquares(self):
        return self.__oppSquares
    def addOppSquare(self, coordinate):
        if((coordinate not in self.__playerSquares) and (coordinate not in self.__oppSquares)):
            self.__oppSquares.append(coordinate)
            return True
        else:
            return False

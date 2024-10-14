
"""
h(n) = 200 * [number of two-side-open-3-in-a-row for me]
     - 80  * [number of two-side-open-3-in-a-row for opponent]
     + 150 * [number of one-side-open-3-in-a-row for me]
     - 40  * [number of one-side-open-3-in-a-row for opponent]
     + 20  * [number of two-side-open-2-in-a-row for me]
     - 15  * [number of two-side-open-2-in-a-row for opponent]
     + 5   * [number of one-side-open-2-in-a-row for me]
     - 2   * [number of one-side-open-2-in-a-row for opponent]
"""

class State():
    def __init__(self, playerSquares, oppSquares):
        self.__playerSquares = playerSquares
        self.__oppSquares = oppSquares
        self.__playerHeuristic = self.genHeuristic(1)
        self.__oppHeuristic = self.genHeuristic(0)
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
    def genHeuristic(self, num):
        return evaluate_state(self, num)
    def getHeuristic(self, num):
        if(num == 1):
            return self.__playerHeuristic
        else:
            return self.__oppHeuristic
    def regenHeur(self):
        self.__playerHeuristic = self.genHeuristic(1)
        self.__oppHeuristic = self.genHeuristic(0)

def evaluate_state(state, player):
    if player == 1:  # Player X
        player_squares = state.getPlayerSquares()
        opp_squares = state.getOppSquares()
    else:  # Player O
        player_squares = state.getOppSquares()
        opp_squares = state.getPlayerSquares()
    #Generating player and opponent sequence counts
    playerSeqs = findSequenceValues(player_squares, opp_squares)
    oppSeqs = findSequenceValues(opp_squares, player_squares)
    #Checking for terminals.
    if(playerSeqs[0] == 1):
        return 1000
    if(oppSeqs[0] == 1):
        return -1000
    if(len(player_squares) + len(opp_squares) == 30):
        return 0
    two_side_open_3_in_a_row_me = playerSeqs[3]
    two_side_open_3_in_a_row_opp = oppSeqs[3]
    one_side_open_3_in_a_row_me = playerSeqs[4]
    one_side_open_3_in_a_row_opp = oppSeqs[4]
    two_side_open_2_in_a_row_me = playerSeqs[1]
    two_side_open_2_in_a_row_opp = oppSeqs[1]
    one_side_open_2_in_a_row_me = playerSeqs[2]
    one_side_open_2_in_a_row_opp = oppSeqs[2]
    #Calculating heuristic score based on quantities of sequences.
    score = (200 * two_side_open_3_in_a_row_me) - (80 * two_side_open_3_in_a_row_opp) + \
            (150 * one_side_open_3_in_a_row_me) - (40 * one_side_open_3_in_a_row_opp) + \
            (20 * two_side_open_2_in_a_row_me) - (15 * two_side_open_2_in_a_row_opp) + \
            (5 * one_side_open_2_in_a_row_me) - (2 * one_side_open_2_in_a_row_opp)

    return score
#Determining if a space is within the game border.
def inBorder(querySpace):
    if(querySpace[0] > 6 or querySpace[0] < 1 or querySpace[1] > 5 or querySpace[1] < 1):
        return False
    else:
        return True
#findSequences
#This function finds each sequence for one player in a state
#The list of sequences is returned without duplicates.
def findSequences(playerSqs):
    sequences = []
    directions = [[0, 1], [1, 1], [1, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [1, -1]]
    for square in playerSqs:
        #Finding adjacencies of each square
        adjacents = adjacentSquares(square, playerSqs, directions)
        
        #Determining whether the sequence continues past a length of two.
        #Utilizes the adjacentSquares function again but only looking in one direction.
        for adjacent in adjacents:
            sequence = [square, adjacent]
            direction = [[(adjacent[0] - square[0]), (adjacent[1]-square[1])]]
            newSquare = adjacentSquares(adjacent, playerSqs, direction)
            if(len(newSquare) == 1):
                sequence.append(newSquare[0])
            direction[0][0] *= -1
            direction[0][1] *= -1
            newSquare = adjacentSquares(square, playerSqs, direction)
            if(len(newSquare) == 1):
                sequence.insert(0, newSquare[0])
            
            #Ensuring no duplicates
            reverse = []
            for element in sequence:
                reverse.append([element[0], element[1]])
            reverse.reverse()
            if((reverse not in sequences) and (sequence not in sequences)):
                sequences.append(sequence)
    return sequences
#adjacentSquqares:
#This function determines
def adjacentSquares(square, squareList, directions):
    adjacentSq = []
    for direction in directions:
        adjacent = [(square[0] + direction[0]), (square[1] + direction[1])]
        if(adjacent in squareList):
            adjacentSq.append(adjacent)
    return adjacentSq
#findSequenceValues:
#This function finds out how many of each type of sequence are on the board
#It is returned in a list of values containing the amount of each sequence type
#returnVal[0] = four in a row
#returnVal[1] = two-side-open-2-in-a-row
#returnVal[2] = one-side-open-2-in-a-row
#returnVal[3] = two-side-open-3-in-a-row
#returnVal[4] = one-side-open-3-in-a-row
def findSequenceValues(playerSqs, opponentSqs):
    sequences = findSequences(playerSqs)
    returnVal = [0,0,0,0,0]
    for sequence in sequences:
        #for each sequence, determine the amount of open spaces on the ends
        openSpaces = 0
        direction = [(sequence[0][0] - sequence[1][0]), (sequence[0][1] - sequence[1][1])]
        querySpace = [sequence[0][0] + direction[0], sequence[0][1] + direction[1]]
        if querySpace not in opponentSqs and inBorder(querySpace):
            openSpaces += 1
        direction = [sequence[-1][0] - sequence[-2][0], sequence[-1][1] - sequence[-2][1]]
        querySpace = [sequence[-1][0] + direction[0], sequence[-1][1] + direction[1]]
        if querySpace not in opponentSqs and inBorder(querySpace):
            openSpaces += 1
            
        #Using length and openSpaces, determine quantity of each sequence type.
        if len(sequence) == 2:
            if openSpaces == 2:
                returnVal[1] += 1
            elif openSpaces == 1:
                returnVal[2] += 1
        elif len(sequence) == 3:
            if openSpaces == 2:
                returnVal[3] += 1
            elif openSpaces == 1:
                returnVal[4] += 1
        elif len(sequence) == 4:
            returnVal[0] = 1
            return returnVal
    return returnVal
        



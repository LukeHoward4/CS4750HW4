class Node():
    def __init__(self, parentNode, state, action, pathCost, depth, player):
        self.__parentNode = parentNode
        self.__state = state
        self.__action = action
        self.__pathCost = pathCost
        self.__depth = depth
        self.__player = player

    def get_parent(self):
        return self.__parentNode
    def get_path_cost(self):
        return self.__pathCost
    def getState(self):
        return self.__state
    def getAction(self):
        return self.__action
    def getDepth(self):
        return self.__depth
    def getPlayer(self):
        return self.__player
    def __lt__(self, other):
        return self.__pathCost < other.get_path_cost() #for comparison of nodes based on path cost
def calculate_path_cost(node):
    total_cost = 0
    while node is not None:
        total_cost += node.get_path_cost()
        node = node.get_parent()
    return total_cost

def findSequence(node):
    actionList = []
    while node is not None:
        actionList.append(node.getAction())
        node = node.get_parent()
    actionList.reverse()
    actionList.pop(0)
    return actionList

def expand(current):
    successors = []
    state = current.getState()  
    depth = current.getDepth() + 1
    current_player = current.getPlayer()  
    
    # Get the list of squares occupied by current player and opponent
    if current_player == 1:
        player_squares = state.getPlayerSquares()
        opp_squares = state.getOppSquares()
    else:
        player_squares = state.getOppSquares()
        opp_squares = state.getPlayerSquares()
    
    # Get the possible moves by finding empty adjacent squares
    empty_squares_with_directions = get_adjacent_empty_squares_with_directions(player_squares, opp_squares)
    
    # Sort moves based on tie-breaking rules: increasing column first, then row
    empty_squares_with_directions.sort(key=lambda x: (x[0][1], x[0][0]))  
    
    # For each possible move, create a new node with the updated state
    for move, direction in empty_squares_with_directions:
        new_state = copy_state(state)  
        
        # Update the new state with the current player's move
        if current_player == 1:
            new_state.addPlayerSquare(move)
        else:
            new_state.addOppSquare(move)
        
        # Create a new node with the updated state, move, path cost, and depth
        action = f"place at {move} ({direction})"  # will give o/p like "place at [2, 3] (up)"
        path_cost = 1.0  # cost = 1 for each move
        new_node = Node(current, new_state, action, path_cost, depth, 3 - current_player)  
        
        successors.append(new_node)
    
    return successors

def get_adjacent_empty_squares_with_directions(player_squares, opp_squares):
    directions = {
        (0, 1): "right",
        (1, 0): "down",
        (0, -1): "left",
        (-1, 0): "up",
        (1, 1): "down-right",
        (1, -1): "down-left",
        (-1, 1): "up-right",
        (-1, -1): "up-left"
    }
    empty_squares_with_directions = []
    all_occupied = player_squares + opp_squares  

    for square in player_squares + opp_squares:
        for direction, name in directions.items():
            adjacent_square = [square[0] + direction[0], square[1] + direction[1]]
            # Check if the adjacent square is within bounds and not already occupied
            if 1 <= adjacent_square[0] <= 5 and 1 <= adjacent_square[1] <= 6 and adjacent_square not in all_occupied:
                if (adjacent_square, name) not in empty_squares_with_directions:
                    empty_squares_with_directions.append((adjacent_square, name))
    
    return empty_squares_with_directions

def copy_state(state):
    new_state = State(state.getPlayerSquares().copy(), state.getOppSquares().copy())
    return new_state


from State import State

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

def evaluate_state(state, player):
    if player == 1:  # Player X
        player_squares = state.getPlayerSquares()
        opp_squares = state.getOppSquares()
    else:  # Player O
        player_squares = state.getOppSquares()
        opp_squares = state.getPlayerSquares()

    two_side_open_3_in_a_row_me = count_two_side_open_3_in_a_row(player_squares, opp_squares)
    two_side_open_3_in_a_row_opp = count_two_side_open_3_in_a_row(opp_squares, player_squares)
    one_side_open_3_in_a_row_me = count_one_side_open_3_in_a_row(player_squares, opp_squares)
    one_side_open_3_in_a_row_opp = count_one_side_open_3_in_a_row(opp_squares, player_squares)
    two_side_open_2_in_a_row_me = count_two_side_open_2_in_a_row(player_squares, opp_squares)
    two_side_open_2_in_a_row_opp = count_two_side_open_2_in_a_row(opp_squares, player_squares)
    one_side_open_2_in_a_row_me = count_one_side_open_2_in_a_row(player_squares, opp_squares)
    one_side_open_2_in_a_row_opp = count_one_side_open_2_in_a_row(opp_squares, player_squares)

    score = (200 * two_side_open_3_in_a_row_me) - (80 * two_side_open_3_in_a_row_opp) + \
            (150 * one_side_open_3_in_a_row_me) - (40 * one_side_open_3_in_a_row_opp) + \
            (20 * two_side_open_2_in_a_row_me) - (15 * two_side_open_2_in_a_row_opp) + \
            (5 * one_side_open_2_in_a_row_me) - (2 * one_side_open_2_in_a_row_opp)

    return score

def findSequences(playerSqs):
    sequences = []
    directions = [[0, 1], [1, 1], [1, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [1, -1]]
    for square in playerSqs:
        adjacents = adjacentSquares(square, playerSqs, directions)
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
            
            reverse = []
            for element in sequence:
                reverse.append([element[0], element[1]])
            reverse.reverse()

            if((reverse not in sequences) and (sequence not in sequences)):
                sequences.append(sequence)
    return sequences
def adjacentSquares(square, squareList, directions):
    adjacentSq = []
    for direction in directions:
        adjacent = [(square[0] + direction[0]), (square[1] + direction[1])]
        if(adjacent in squareList):
            adjacentSq.append(adjacent)
    return adjacentSq


playerSqs = [[1, 2], [1, 1], [1, 0], [2, 1],[3, 5]]
print([1, 2] in playerSqs)
print(findSequences(playerSqs))

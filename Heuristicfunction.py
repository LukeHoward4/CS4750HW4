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

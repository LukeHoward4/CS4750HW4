import time
from State import State
from Node import Node, expand
from minimax import minimax2, minimax4


def print_board(player_squares, opp_squares):
    board = [["." for _ in range(6)] for _ in range(5)]  
    for square in player_squares:
        board[square[0] - 1][square[1] - 1] = "X"  
    for square in opp_squares:
        board[square[0] - 1][square[1] - 1] = "O"  

    for row in board:
        print(" ".join(row))
    print()

def play_game():

    player_squares = [[3, 4]]  # Player 1 at [3, 4]
    opp_squares = [[3, 3]]     # Player 2 at [3, 3]

    current_state = State(player_squares, opp_squares)
    current_node = Node(None, current_state, "start", 0.0, 0, 1)  
    game_over = False
    move_number = 1

    while not game_over:
        print(f"Move {move_number}:")
        print("Current board:")
        print_board(current_state.getPlayerSquares(), current_state.getOppSquares())

        start_time = time.time()

        # minmax algorithm
        if current_node.getPlayer() == 1:
            print("Player 1's turn:")
            best_move = minimax2(current_node, 1)
        else:
            print("Player 2's turn:")
            best_move = minimax4(current_node, 0)
        x = best_move.getState().getHeuristic(current_node.getPlayer())
        print(best_move.getAction())
        print("Heuristic: " + str(x))
        print(current_node.getPlayer())
        print(best_move.getState().getPlayerSquares())
        if(best_move.getState().getHeuristic(current_node.getPlayer()) == 1000):
            print(f"Player {current_node.getPlayer()} wins!")
            game_over = True
        
        action = best_move.getAction()
        current_state = best_move.getState()
        current_node = best_move
        
        end_time = time.time()
        cpu_time = end_time - start_time
        
        print(f"Action: {action}")
        print(f"CPU time: {cpu_time:.4f} seconds")
        print(f"Nodes generated: {len(expand(current_node))}")
        if(current_state.getHeuristic(current_node.getPlayer()) == 1000):
            print(f"Player {current_node.getPlayer()} wins!")
        print()
        

        move_number += 1

        # Check for game over condition (e.g., win, draw, max moves)
        if move_number >= 50:  #  End the game after a 50 moves
            game_over = True

    print("Game over!")
    print("Final board:")
    print_board(current_state.getPlayerSquares(), current_state.getOppSquares())

if __name__ == "__main__":
    play_game()

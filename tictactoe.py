"""
Tic-Tac-Toe AI Player
=====================
An unbeatable Tic-Tac-Toe AI implemented using the Minimax algorithm 
optimized with Alpha-Beta Pruning.

Author: Parth Rajput
"""

import math
from typing import List, Tuple, Optional


class TicTacToe:
    def __init__(self):
        # 3x3 board initialized with empty spaces
        self.board: List[str] = [' ' for _ in range(9)]
        self.current_winner: Optional[str] = None

    def print_board(self) -> None:
        """Prints the current state of the board."""
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums() -> None:
        """Prints the indices corresponding to each cell on the board."""
        # 0 | 1 | 2 etc.
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self) -> List[int]:
        """Returns a list of available move indices."""
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self) -> bool:
        """Checks if there are empty squares left on the board."""
        return ' ' in self.board

    def num_empty_squares(self) -> int:
        """Returns the number of empty squares."""
        return self.board.count(' ')

    def make_move(self, square: int, letter: str) -> bool:
        """Places a letter on the board if the move is valid."""
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square: int, letter: str) -> bool:
        """Validates if the current move creates a winning combination."""
        # Check row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True

        return False


class SmartAIPlayer:
    def __init__(self, letter: str):
        self.letter = letter

    def get_move(self, game: TicTacToe) -> int:
        """Calculates the optimal move using Minimax with Alpha-Beta Pruning."""
        if game.num_empty_squares() == 9:
            # Optimal first move for Tic-Tac-Toe is usually the corner or center.
            # Choosing center (4) for a strong start if AI moves first.
            return 4
        
        # Initializing Alpha and Beta for optimization
        alpha = -math.inf
        beta = math.inf
        
        state = self.minimax(game, self.letter, alpha, beta)
        return state['position']

    def minimax(self, game: TicTacToe, player: str, alpha: float, beta: float) -> dict:
        """Core Minimax Algorithm with Alpha-Beta Pruning."""
        max_player = self.letter  # The AI itself
        other_player = 'O' if player == 'X' else 'X'

        # Base cases: Check if the previous move won the game
        if game.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (game.num_empty_squares() + 1) if other_player == max_player 
                         else -1 * (game.num_empty_squares() + 1)
            }
        elif not game.empty_squares():
            return {'position': None, 'score': 0}

        # Initialize dictionaries to track the best score
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Maximize
        else:
            best = {'position': None, 'score': math.inf}   # Minimize

        for possible_move in game.available_moves():
            # Step 1: Make a simulated move
            game.make_move(possible_move, player)
            
            # Step 2: Recurse using minimax
            sim_score = self.minimax(game, other_player, alpha, beta)
            
            # Step 3: Undo the simulated move
            game.board[possible_move] = ' '
            game.current_winner = None
            sim_score['position'] = possible_move  # Update position reference

            # Step 4: Alpha-Beta Pruning and Score Updates
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
                alpha = max(alpha, sim_score['score'])
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                beta = min(beta, sim_score['score'])
            
            if beta <= alpha:
                break  # Prune the branch

        return best


class HumanPlayer:
    def __init__(self, letter: str):
        self.letter = letter

    def get_move(self, game: TicTacToe) -> int:
        """Gets a valid move index from human console input."""
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"Your turn ({self.letter}). Move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val


def play(game: TicTacToe, x_player, o_player, print_game=True) -> Optional[str]:
    """Main game loop orchestration."""
    if print_game:
        game.print_board_nums()
        print("-" * 15)

    letter = 'X'  # Starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print("-" * 15)

            if game.current_winner:
                if print_game:
                    print(f"Game Over! {letter} wins!")
                return letter

            # Switch turns
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It's a tie!")
    return None


if __name__ == '__main__':
    # Initialize players: Human plays as X, Smart AI plays as O
    x_player = HumanPlayer('X')
    o_player = SmartAIPlayer('O')
    tictactoe_game = TicTacToe()
    
    print("Welcome to Unbeatable Tic-Tac-Toe AI!")
    play(tictactoe_game, x_player, o_player, print_game=True)
# Constants
X = 'X'
O = 'O'

class Tictactoe:
    """
    Tictactoe contains the game model.
    All the function related to the game's structure is in this class.
    """

    def __init__(self):
        """
        Initializes a new Tictactoe game. Creates player and board.
        """
        # Current player
        self.player = X

        # Board
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def get_board(self):
        """
        Get function for board

        Returns:
            Nested list (3 x 3): board
        """
        return self.board.copy()
    
    def is_valid_action(self, action):
        """
        Checks if the action is valid

        Args:
            action (tuple (i, j)): coordinates of a cell

        Returns:
            bool: True if the action is valid, False otherwise
        """
        if self.board[action[0]][action[1]] == None:
            return True
        
        return False

    def action(self, action):
        """
        Performs the given action if valid

        Args:
            action (tuple (i, j)): coordinates of a cell

        Raises:
            Exception: If action is invalid
        """
        if self.is_valid_action(action):
            # Modify the board
            self.board[action[0]][action[1]] = self.player

            # Switch player
            self.player = X if self.player == O else O
        else:
            raise Exception('Invalid action')

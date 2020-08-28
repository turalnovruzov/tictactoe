class Tictactoe:
    """
    Tictactoe contains the game model.
    All the function related to the game's structure is in this class.
    """

    def __init__(self):
        """
        Initializes a new Tictactoe game. Creates player and board.
        """
        # Constants
        self.X = 'X'
        self.O = 'O'

        # Current player
        self.player = self.X

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

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

        # Winner
        self.winner = None

        # Game over
        self._gameover = False

    def get_board(self):
        """
        Get function for board

        Returns:
            Nested list (3 x 3): board
        """
        return self.board.copy()
    
    def get_winner(self):
        """Get function for winner

        Returns:
            str: 'X' or 'O'
        """
        return self.winner
    
    @classmethod
    def available_actions(cls, board):
        """
        Finds all the available actions for the given board

        Args:
            board (nested list (3 x 3)): a Tictactoe board

        Returns:
            list of tuples (i, j): the available actions
        """
        actions = []

        # Loop through the board
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    actions.append((i, j))
        
        return actions
    
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
    
    def terminal(self):
        """
        Check s if the curretn state is terminal

        Returns:
            bool: True if terminal, False otherwise
        """
        # Horizontal check
        for i in range(3):
            b_ = True
            for j in range(2):
                if self.board[i][j] == None or self.board[i][j] != self.board[i][j + 1]:
                    b_ = False
            
            if b_:
                self.winner = self.board[i][0]
                return True
        
        # Vertical check
        for j in range(3):
            b_ = True
            for i in range(2):
                if self.board[i][j] == None or self.board[i][j] != self.board[i + 1][j]:
                    b_ = False
            
            if b_:
                self.winner = self.board[0][j]
                return True
        
        # Diagonal check
        if self.board[1][1] != None:
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                self.winner = self.board[1][1]
                return True

            if self.board[2][0] == self.board[1][1] == self.board[0][2]:
                self.winner = self.board[1][1]
                return True

        # Draw check
        if sum([row.count(None) for row in self.board]) == 0:
            self.winner = None
            return True
        
        return False
    
    def gameover(self):
        """
        Checks if the game is over

        Returns:
            bool: True if game over, False otherwise
        """
        if self._gameover:
            return True
        
        if self.terminal():
            self._gameover = True
            return True
        
        return False

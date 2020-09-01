def state_to_tuple(state):
    """
    Converst state to nested tuples

    Args:
        state (nested list (3 x 3)): the state

    Returns:
        nested tuple (3 x 3): the state converted to nested tuple
    """
    return (tuple(row) for row in state)


class QAgent:
    """
    A q-learning agent for Tictactoe
    """

    def __init__(self, alpha, epsilon):
        """
        Initializes the QAgent

        Args:
            alpha (float): Learning rate
            epsilon (float): Probability of choosing a random action
        """
        self.alpha = alpha
        self.epsilon = epsilon

        # Q table
        self.Q = dict()
    
    def get_q_value(self, state, action):
        # Convert state to tuple
        tpl = state_to_tuple(state)

        # If (state, action) in Q return value, else return 0
        if (state_to_tuple(state), action) in self.Q:
            return self.Q[tpl, action]

        return 0

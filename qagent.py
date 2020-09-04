import random
import pickle
import os
from tictactoe import Tictactoe


def state_to_tuple(state):
    """
    Converst state to nested tuples

    Args:
        state (nested list (3 x 3)): the state

    Returns:
        nested tuple (3 x 3): the state converted to nested tuple
    """
    return tuple(tuple(row) for row in state)


class QAgent:
    """
    A q-learning agent for Tictactoe
    """

    def __init__(self, alpha=0.5, epsilon=0.1):
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

        # Create agents directory
        self.agent_dir = 'agents'
        if not os.path.isdir(self.agent_dir):
            os.mkdir(self.agent_dir)
    
    def load(self, filepath='Q.pkl'):
        """
        Loads Q table from file

        Args:
            filepath (str, optional): the file's path. Defaults to 'Q.pkl'.
        """
        try:
            with open(os.path.join(self.agent_dir, filepath), 'rb') as file:
                self.Q = pickle.load(file)
        except FileNotFoundError:
            print(f'{filepath} does not exist.')
            exit()
        except:
            print(f'{filename} does not contain an agent.')
            exit()
    
    def save(self, filepath='Q.pkl'):
        """
        Saves Q table to file

        Args:
            filepath (str, optional): the file's path. Defaults to 'Q.pkl'.
        """
        with open(os.path.join(self.agent_dir, filepath), 'wb') as file:
            pickle.dump(self.Q, file, protocol=pickle.HIGHEST_PROTOCOL)
    
    def get_q_value(self, state, action):
        """
        Gets the Q value for the state and action

        Args:
            state (nested list (3 x 3)): a Tictactoe board
            action (tuple (i, j)): indexes of a cell in the state

        Returns:
            float: the Q value
        """
        # Convert state to tuple
        tpl = state_to_tuple(state)

        # If (state, action) in Q return value, else return 0
        if (state_to_tuple(state), action) in self.Q:
            return self.Q[tpl, action]

        return 0
    
    def future_rewards(self, state):
        """
        Calculates the maximum reward of state

        Args:
            state (nested list (3 x 3)): a Tictactoe board

        Returns:
            float: maximum reward
        """
        # Get all the available ations
        actions = Tictactoe.available_actions(state)

        # Return 0 if not actions available
        if len(actions) == 0:
            return 0

        # Choose the max reward according to the Q table
        max_reward = self.get_q_value(state, actions[0])

        for action in actions:
            value = self.get_q_value(state, action)

            if value > max_reward:
                max_reward = value
        
        return max_reward
    
    def update_q_value(self, state, action, new_state, reward):
        # Get the old q value
        old_q = self.get_q_value(state, action)

        # Convert state to tuple
        tpl_state = state_to_tuple(state)

        self.Q[tpl_state, action] = old_q + self.alpha * ((reward + self.future_rewards(new_state)) - old_q)
    
    def best_action(self, state, epsilon_true=False):
        """
        Chooses the best action according to the state

        Args:
            state (nested list (3 x 3)): a Tictactoe board

        Raises:
            Exception: If no action is available

        Returns:
            tuple (i, j): best action
        """
        # Get all the available ations
        actions = Tictactoe.available_actions(state)

        # Raise if no action available
        if len(actions) == 0:
            raise Exception('No action available')

        # Choose the best action according to its Q value
        if (not epsilon_true) or (epsilon_true and random.random() < (1 - self.epsilon)):

            best_action = actions[0]
            max_reward = self.get_q_value(state, best_action)

            for action in actions:
                value = self.get_q_value(state, action)

                if value > max_reward or (value == max_reward and random.random() < 0.5):
                    best_action = action
                    max_reward = value
        
        # Randomly choose the best action
        else:
            best_action = random.choice(actions)
        
        return best_action
    
    def train(self, num_games):
        """
        Trains the agent by playing games against itself

        Args:
            num_games (int): number of games to train
        """

        # Play num_games games
        for n in range(num_games):

            # Print game number
            if n % 1000 == 0:
                print(f'Game #{n + 1}')
            
            # Initialize the game
            ttt = Tictactoe()

            # Keep track of last state and actions
            last = {
                'X': {'state': None, 'action': None},
                'O': {'state': None, 'action': None}
            }

            # Play the game
            while True:

                # Get the state and action
                state = ttt.get_board()
                action = self.best_action(state, epsilon_true=True)

                # Save as lasts
                last[ttt.get_player()]['state'] = state
                last[ttt.get_player()]['action'] = action

                # Apply action and get the new state
                ttt.action(action)
                new_state = ttt.get_board()

                # Game over
                if ttt.gameover():

                    # Won the game
                    if ttt.get_winner() is not None:

                        # Update q value for winner
                        self.update_q_value(state, action, new_state, 1)

                        # Update q value for loser
                        self.update_q_value(
                            last[ttt.get_player()]['state'],
                            last[ttt.get_player()]['action'],
                            new_state, -1
                        )
                    
                    # Draw
                    else:
                        # Update q value
                        self.update_q_value(state, action, new_state, 0)
                    
                    break
                
                # Game continues
                elif last[ttt.get_player()]['state'] is not None:

                    # Update last action
                    self.update_q_value(
                        last[ttt.get_player()]['state'],
                        last[ttt.get_player()]['action'],
                        new_state, 0
                    )
        
        print('Training done')

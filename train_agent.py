import argparse
from qagent import QAgent


def check_episodes(episodes):
    """
    Checks the validity of the episodes command line argument
    """
    episodes = int(episodes)
    if episodes < 0:
        raise argparse.ArgumentTypeError(f'{episodes} is an invalid episodes value')
    return episodes

def check_alpha(alpha):
    """
    Checks the validity of the alpha command line argument
    """
    alpha = float(alpha)
    if alpha <= 0:
        raise argparse.ArgumentTypeError(f'{alpha} is an invalid alpha value')
    return alpha

def check_epsilon(epsilon):
    """
    Checks the validity of the epsilon command line argument
    """
    epsilon = float(epsilon)
    if not (0 <= epsilon <= 1):
        raise argparse.ArgumentTypeError(f'{epsilon} is an invalid epsilon value')
    return epsilon


# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('episodes', type=check_episodes, help='Number of games to train.')
parser.add_argument('-f', type=str, default='Q.pkl', metavar='FILEPATH', dest='filepath',
                    help='Full or relative path of a file in which the agent is (to be) stored. Defaults to \"Q.pkl\"')
parser.add_argument('-l', dest='load', action='store_true', help='Load agent from file.')
parser.add_argument('-a', type=check_alpha, dest='alpha', metavar='ALPHA', default=0.5,
                    help='Learning rate. Must be float and strictly grater than 0. Defaults to 0.5.')
parser.add_argument('-e', type=check_epsilon, dest='epsilon', metavar='EPSILON', default=0.1,
                    help='Epsilon randomness value. Must be float and between and including 0 and 1. Defaults to 0.1.')
args = parser.parse_args()

agent = QAgent(alpha=args.alpha, epsilon=args.epsilon)

if args.load:
    try:
        agent.load(args.filepath)
    except FileNotFoundError:
        print(f'{args.filepath} does not exist. Not loading agent from file.')

agent.train(args.episodes)

agent.save(args.filepath)

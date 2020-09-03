import argparse
from qagent import QAgent


def check_episodes(episodes):
    """
    Checks the validity of the episodes command line argument

    Args:
        episodes (str): command line argument value

    Raises:
        argparse.ArgumentTypeError: If episodes value is invalid

    Returns:
        int: episodes
    """
    episodes = int(episodes)
    if episodes < 0:
        raise argparse.ArgumentTypeError(f'{episodes} is an invalid episodes value')
    return episodes


# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('episodes', type=check_episodes, help='Number of games to train')
parser.add_argument('-f', type=str, default='Q.pkl', metavar='FILEPATH', dest='filepath',
                    help='Full or relative path of a file in which the agent is stored. Defaults to \"Q.pkl\"')
parser.add_argument('-l', dest='load', action='store_true', help='Load agent from file')
args = parser.parse_args()

agent = QAgent()

if args.load:
    agent.load(args.filepath)

agent.train(args.episodes)

agent.save(args.filepath)

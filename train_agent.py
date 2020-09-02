import argparse
from qagent import QAgent

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filepath', type=str, default='Q.pkl',
                    help='Full or relative path of a file in which the agent is stored')
parser.add_argument('-l', '--load', action='store_true', help='Load agent from file')
args = parser.parse_args()

agent = QAgent

if args.load:
    agent.load(args.filepath)

agent.save(args.filepath)

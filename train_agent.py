import argparse
from qagent import QAgent

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filepath', type=str, default='Q.pkl',
                    help='Full or relative path of a file in which the agent is stored')
args = parser.parse_args()

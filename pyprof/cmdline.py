import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='profile an app')
    # the parser might take an already computed .prof file or
    # run the program directly, see what's the best approach

    parser.add_argument('-i', '--interactive',
                        action='store_true')

    parser.add_argument('-fi', '--filter_include',
                        help='list of modules to include')

    parser.add_argument('-fe', '--filter_exclude',
                        help='list of modules to exclude')

    return parser.parse_args()


def main():
    ns = parse_arguments()

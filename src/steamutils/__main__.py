"""The CLI entry of steamutils."""
from argparse import ArgumentParser

from ._version import __version__ as version


def main(argv=None):
    """Tools for performing analytics on steam users, steam groups and servers using the SteamAPI and various popular SourceMod plugins"""
    parser = ArgumentParser()
    parser.description = main.__doc__
    parser.add_argument("-p", "--print", action="store_true", help="print hello world")
    parser.add_argument("-V", "--version", action="version", version=version)
    args = parser.parse_args(argv)

    print(f"testing: Hello world! {args}")


def init():
    """For unit test only."""
    if __name__ == "__main__":
        main()


init()

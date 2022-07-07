"""Class for normalizing the various formats for a SteamID"""


class NotASteamIDException(Exception):
    pass


class SteamID:
    def __init__(self, identifier: int | str) -> None:
        pass

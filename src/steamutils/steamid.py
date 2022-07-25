"""
Class for normalizing the various formats for a SteamID

A `SteamID` (or just id) will refer to the format `STEAM_X:Y:Z` where `X` represents the
"Universe" the account belongs to, `Y` represents a checkdigit of the account
number, either a 1 or 0, and `Z` represents the account number.
    e.g. "STEAM_0:0:84901"

A SteamID64 (or just id64) will refer to the SteamID converted to a 64 bit
integer `W` such that `W=Z*2+V+Y` where `Y` represents a checkdigit of the
account number, either a 1 or 0, `Z` represents the account number, and `V`
represents a constant identifier.
    e.g. "76561197960435530"

A Steam3 ID (or just id3) will refer to the newer SteamID notation of the
format `[type:1:W]` such that `W=Z*2+Y` where `Y` represents a checkdigit of
the account number, either a 1 or 0, and `Z` represents the account number.
    e.g. "[U:1:169802]"

"""

import re


class NotASteamIDException(Exception):
    pass


class SteamID:

    ID64_INDIVIDUAL_IDENTIFIER = 0x0110000100000000
    ID64_CLAN_IDENTIFIER = 0x0170000000000000

    RE_ID = re.compile(r"STEAM_(?P<universe>[0-5]):(?P<checkdigit>[01]):(?P<account>\d+)")
    RE_ID3 = re.compile(r"\[?(?P<account_type>[IUMGAPCgTLca]):1:(?P<encode32>\d+)\[?")
    RE_ID64 = re.compile(r"((https?://)?steamcommunity.com/profiles/)?(?P<id64>\d+)([/?].*)?")

    RE_URL_VANITY = re.compile(r"(https?://)?steamcommunity.com/id/(?P<vanity>.+)")

    id: str
    id3: str
    id64: int

    def __init__(self, identifier: int | str) -> None:
        account = 0
        universe = 0
        account_type = "U"
        checkdigit = 0

        identifier = str(identifier)

        if parse := re.match(self.RE_ID, identifier):
            # normalize from SteamID
            account = int(parse.group("account"))
            checkdigit = int(parse.group("checkdigit"))

            # unused
            universe = int(parse.group("universe"))

        elif parse := re.match(self.RE_ID3, identifier):
            # normalize from Steam3 ID
            encode32 = int(parse.group("encode32"))
            account = encode32 // 2
            checkdigit = encode32 % 2

            # unused
            account_type = parse.group("account_type")

        elif parse := re.match(self.RE_ID64, identifier):
            # normalize from SteamID64 or steamcommunity url that contains SteamID64
            id64 = int(parse.group("id64"))
            account = (id64 - self.ID64_INDIVIDUAL_IDENTIFIER) // 2
            checkdigit = id64 % 2

        else:
            raise NotASteamIDException(f'SteamID for "{identifier}" could not be found')

        encode32 = (account * 2) + checkdigit

        self.id = f"STEAM_{universe}:{checkdigit}:{account}"
        self.id3 = f"[{account_type}:1:{encode32}]"
        self.id64 = encode32 + self.ID64_INDIVIDUAL_IDENTIFIER

    @property
    def steam_url(self) -> str:
        """Returns a url to the Steam Profile that corresponds to this SteamID"""
        return f"https://steamcommunity.com/profiles/{self.id64}"

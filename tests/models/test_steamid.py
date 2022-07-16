import pytest

from steamutils.models import SteamID, NotASteamIDException

ROBIN = ("STEAM_0:0:84901", "[U:1:169802]", 76561197960435530)
ROBIN_PLUS_ONE = ("STEAM_0:1:84901", "[U:1:169803]", 76561197960435531)


@pytest.mark.parametrize("identifier, id, id3, id64", [
    ("STEAM_0:0:84901", *ROBIN),
    ("STEAM_0:1:84901", *ROBIN_PLUS_ONE),
    ("[U:1:169802]", *ROBIN),
    ("[U:1:169803]", *ROBIN_PLUS_ONE),
    ("U:1:169802", *ROBIN),
    (76561197960435530, *ROBIN),
    (76561197960435531, *ROBIN_PLUS_ONE),
    ("76561197960435530", *ROBIN),
    ("https://steamcommunity.com/profiles/76561197960435530", *ROBIN),
    ("https://steamcommunity.com/profiles/76561197960435531", *ROBIN_PLUS_ONE),
    ("http://steamcommunity.com/profiles/76561197960435530", *ROBIN),
    ("steamcommunity.com/profiles/76561197960435530", *ROBIN),
    ("https://steamcommunity.com/profiles/76561197960435530/", *ROBIN),
    ("https://steamcommunity.com/profiles/76561197960435530?crap=foo&bar=baz", *ROBIN),

])
def test_steamid_from_steamid3(identifier, id, id3, id64):
    """expect a SteamID can be parsed from various formats"""

    s = SteamID(identifier)

    assert s.id == id
    assert s.id3 == id3
    assert s.id64 == id64
    assert s.steam_url == f"https://steamcommunity.com/profiles/{id64}"


def test_steamid_not_found():
    """if the provided input cannot be normalized into a SteamID expect a
    NotASteamIDException to be raised"""

    with pytest.raises(NotASteamIDException):
        SteamID("XXXFOO_0:0:84901")


@pytest.mark.skip()
def test_steamid_from_vanity():
    """expect a SteamID can be parsed from a steam vanity id """

    # TODO: mock vanity api check
    s = SteamID("foobar")

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


@pytest.mark.skip()
def test_steamid_from_vanity_url():
    """expect a SteamID can be parsed from a steam vanity url"""

    # TODO: mock vanity api check
    s = SteamID("https://steamcommunity.com/id/foobar/")

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530

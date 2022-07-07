import pytest

from steamutils.models import SteamID, NotASteamIDException


def test_steamid_from_steamid():
    """expect a SteamID can be parsed from a regular steamid"""

    s = SteamID("STEAM_0:0:84901")

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


def test_steamid_from_steamid3():
    """expect a SteamID can be parsed from a steamid3"""

    s = SteamID("[U:1:169802]")

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


def test_steamid_from_steamid64():
    """expect a SteamID can be parsed from a steamid64 """

    s = SteamID(76561197960435530)

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


def test_steamid_from_profiel_url():
    """expect a SteamID can be parsed from a steam profile url """

    s = SteamID("https://steamcommunity.com/profiles/76561197960435530")

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


def test_steamid_from_vanity():
    """expect a SteamID can be parsed from a steam vanity id """

    # TODO: mock vanity api check
    s = SteamID("foobar")

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


def test_steamid_from_vanity_url():
    """expect a SteamID can be parsed from a steam vanity url"""

    # TODO: mock vanity api check
    s = SteamID("https://steamcommunity.com/id/foobar/")

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


def test_steamid_not_found():
    """if the provided input cannot be normalized into a SteamID expect a
    NotASteamIDException to be raised"""

    with pytest.raises(NotASteamIDException):
        SteamID("STEAM_0:0:84901")

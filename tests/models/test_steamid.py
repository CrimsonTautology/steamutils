import pytest

from steamutils.models import SteamID, NotASteamIDException


def test_steamid_from_steamid():
    """expect a SteamID can be parsed from a regular steamid"""

    s = SteamID("STEAM_0:0:84901")

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


@pytest.mark.skip()
@pytest.mark.parametrize("identifier", ["[U:1:169802]", "U:1:169802"])
def test_steamid_from_steamid3(identifier):
    """expect a SteamID can be parsed from a steamid3"""

    s = SteamID(identifier)

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


@pytest.mark.skip()
@pytest.mark.parametrize("identifier", [76561197960435530, "76561197960435530"])
def test_steamid_from_steamid64(identifier):
    """expect a SteamID can be parsed from a steamid64 """

    s = SteamID(identifier)

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


@pytest.mark.skip()
@pytest.mark.parametrize("identifier", [
    "https://steamcommunity.com/profiles/76561197960435530",
    "http://steamcommunity.com/profiles/76561197960435530",
    "steamcommunity.com/profiles/76561197960435530",
])
def test_steamid_from_profiel_url(identifier):
    """expect a SteamID can be parsed from a steam profile url """

    s = SteamID("")

    assert s.id == "STEAM_0:0:84901"
    assert s.id3 == "[U:1:169802]"
    assert s.id64 == 76561197960435530


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


def test_steamid_not_found():
    """if the provided input cannot be normalized into a SteamID expect a
    NotASteamIDException to be raised"""

    with pytest.raises(NotASteamIDException):
        SteamID("XXXFOO_0:0:84901")

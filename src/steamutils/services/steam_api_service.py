import requests
from urllib.parse import urljoin

from steamutils.models import SteamID


def get_owned_games():
    pass


def get_player_achievements():
    pass


def get_friend_list():
    pass


def get_player_summaries():
    pass


def get_steam_level(steamid: SteamID, key: str) -> int:
    response = SteamAPIService.get(
        "IPlayerService", "GetSteamLevel", key, params={"steamid": steamid.id64}
    )
    data = response.json()

    return data["response"]["player_level"]


class SteamAPIService:
    """
    Service for making queires against the Steam API.
    """

    ROOT_URL = "https://api.steampowered.com"

    @classmethod
    def get(
        cls, interface: str, method: str, key: str, version: str = "v1", params=None, **kwargs
    ) -> requests.Response:
        params = params or {}
        route = "/".join(s.strip("/") for s in [interface, method, version])
        url = urljoin(cls.ROOT_URL, route)

        response = requests.get(url, params={"key": key, **params}, **kwargs)

        response.raise_for_status()

        return response

"""Tools for performing analytics on steam users, steam groups and servers using the SteamAPI and various popular SourceMod plugins"""

from .__main__ import main
from ._version import __version__
from .steamid import SteamID, NotASteamIDException

__all__ = [
    "NotASteamIDException",
    "SteamID",
    "__version__",
    main.__name__,
]

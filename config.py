"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "30622042")
        self.API_HASH: str = os.environ.get("API_HASH", "49c4717a6d4937985a2985b16a777d6f")
        self.SESSION: str = os.environ.get("SESSION", "BQHTQVoAmAj-6VUYmkH50dDEl6Mhzd7odx_2-OFuM6lUm8ZcipwVdIZhxm8-Szk_hvOfM2K7GggziKViD7h3CrnnN-60oEaM70NaEajpUh47VGNRId2AGLi5Owa2LJgDJI3CJ8IabXIkV9rS4CG4LCux3eSmL0mJ6YskjR2q0Y13ZSyMk2GX5WC98ltkzXVrPXpA_UTNRjqvmumuRGOhH5uCCVPlyTPfFnz4w7wlOPohUDhRzj2nC0yCmm3OMoYoFwO_3ftA9WH52nH6uMFIpReVNw7lssAKEtgDNx81sgn9B3Dfat1U2-8khHeHrTqTx4_xughrOt14PBy9Cc4d_OM8u9qVtgAAAAIH50BzAA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "8336931089:AAFaz5OjkN8b8oW5Kl6B5SRmaWbhmX1nbxA")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()

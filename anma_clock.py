import asyncio
import time

import datetime

from idotmatrix import ConnectionManager
from idotmatrix import Chronograph
from idotmatrix import Clock
from idotmatrix import Common
from idotmatrix import Countdown

# from idotmatrix import Eco
from idotmatrix import FullscreenColor
from idotmatrix import Gif
from idotmatrix import Graffiti
from idotmatrix import Image

# from idotmatrix import MusicSync
from idotmatrix import Scoreboard

# from idotmatrix import System
from idotmatrix import Text


async def main():
    # connect
    conn = ConnectionManager()
    # for Debug and finding Device
    # await conn.scan()
    # await conn.connectBySearch()
    await conn.connectByAddress(
        address="36:F1:7D:F3:04:3B", # Adresse von IDM-F3043B
    )
    # settings
    test = Common()
    await test.setTime(
        year = datetime.datetime.now().year,
        month = datetime.datetime.now().month,
        day = datetime.datetime.now().day,
        hour = datetime.datetime.now().hour,
        minute = datetime.datetime.now().minute,
        second = datetime.datetime.now().second,
    )
    await test.setBrightness(90)
    # clock
    test = Clock()
    await test.setMode(
        style = 4,
        visibleDate = False,
        hour24 = True,
        r = 26,
        g = 222,
        b = 62,
    )
    await conn.disconnect()
    #time.sleep(5)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        quit()

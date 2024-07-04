import asyncio
import time
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
    # Test mit einer anderen Schriftart und Größe
    test = Text()
    await test.setMode(
        "Franz jagt im völlig verwahrlosten Taxi quer durch München?",
        font_path="./fonts/JetbrainsMonoRegular-RpvmM.ttf",
        font_size=24,
        speed=95,
    )
    time.sleep(5)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        quit()

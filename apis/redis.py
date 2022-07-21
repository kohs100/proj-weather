import aioredis
import asyncio

from secret import Secret
from apis.weather import Forecast
from apis.times import *

class Cache():
    def __init__(self, host, port):
        self._db = aioredis.from_url(f"redis://{host}:{port}")

    async def get(self, nx, ny):
        key = str(btime()) + "%03d%03d" % (nx, ny)
        res = await self._db.setnx(key, "LOCKED")

        if res:
            # 치환 성공. 소유권 획득
            fcst = Forecast(nx, ny)
            await self._db.set(key, fcst.json())
            return fcst.json()
        else:
            res = await self._db.get(key)
            if res == 'LOCKED':
                asyncio.sleep(1)
                pass
            else:
                return res
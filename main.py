import aiohttp
from fastapi import FastAPI

from secret import Secret

from apis.coord import Lamcproj
from apis.redis import Cache
from apis.weather import Forecast


cache = Cache(Secret.redis_url, Secret.redis_port)
lamcproj = Lamcproj()
app = FastAPI()

@app.get("/cachetest")
async def cachetest():
    res = await cache.get(3, 4)
    print(res)
    return res

@app.get("/getUltraSrtFcst")
async def UltraSrtFcst(lon: float, lat: float):
    X, Y = lamcproj.conv(lon, lat)
    
    fcst = Forecast(Secret.key, X, Y)
    return fcst.json()
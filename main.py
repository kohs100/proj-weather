from re import L
from fastapi import FastAPI

from secret import Secret

from apis.coord import Lamcproj
from apis.redis import Cache
from apis.weather import Forecast

cache = Cache(Secret.redis_url, Secret.redis_port)
lamcproj = Lamcproj()
app = FastAPI()

@app.get("/getUltraSrtFcst")
async def UltraSrtFcst(lon: float, lat: float):
    X, Y = lamcproj.conv(lon, lat)
    
    fcst = Forecast(Secret.key, X, Y)
    return fcst.json()
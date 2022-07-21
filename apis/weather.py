import aiohttp
import json

from apis.times import *
from secret import Secret

URL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'

sess = None

async def getUltraSrtFcst(nx, ny):
    params = {
        'serviceKey': Secret.key,
        'numOfRows': '100',
        'pageNo': '1',
        'dataType': 'JSON',
        'base_date': bdate(),
        'base_time': btime(),
        'nx': str(nx),
        'ny': str(ny)
    }

    global sess
    if not sess:
        sess = aiohttp.ClientSession()

    async with sess.get(URL, params=params) as res:
        if res.status != 200:
            raise ValueError("Request failed")
        data = res.json()
        
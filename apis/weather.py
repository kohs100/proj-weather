import requests as r
import json
from datetime import datetime
from pytz import timezone

URL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'

class Forecast():
    def __init__(self, key, nx, ny):
        dt = datetime.now(timezone('Asia/Seoul'))
        bdate = dt.strftime('%Y%m%d')
        btime = dt.strftime('%H%M')

        self.params = {
            'serviceKey': key,
            'numOfRows': '100',
            'pageNo': '1',
            'dataType': 'JSON',
            'base_date': bdate,
            'base_time': btime,
            'nx': str(nx),
            'ny': str(ny)
        }

        self.resp = r.get(URL, params=self.params)

        if self.resp.status_code != 200:
            raise ValueError('API Failed')
    
    def json(self):
        return self.resp.json()

# test
if __name__ == '__main__':
    fcst = Forecast(66, 100)

    with open('res.json', 'w') as f:
        json.dump(fcst.json(), f)
        
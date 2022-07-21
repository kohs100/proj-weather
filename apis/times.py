from datetime import datetime
from pytz import timezone

def btime(round=True):
    dt = datetime.now(timezone('Asia/Seoul'))
    btime = dt.strftime('%H%M')
    if round:
        tm = int(btime[2])

        if tm < 3:
            return btime[:2] + "00"
        else:
            return btime[:2] + "30"

    return btime

def bdate():
    dt = datetime.now(timezone('Asia/Seoul'))
    return dt.strftime('%Y%m%d')

def bdatetime():
    dt = datetime.now(timezone('Asia/Seoul'))
    bdate = dt.strftime('%Y%m%d')
    btime = dt.strftime('%H%M')

    return bdate, btime
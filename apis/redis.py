import aioredis

class Cache():
    def __init__(self, host, port):
        self._db = aioredis.from_url(f"redis://{host}:{port}")
    
    # TODO: 쿼리 캐시 스키마 결정
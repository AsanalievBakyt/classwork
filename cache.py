

import time

cache ={
    'a': 5,
    'b': 10,
    'c': 11,
    'z': 20

}

def session(cache,sec):
    start = time.time()
    for i in range(sec):
        time.sleep(1)
        loop_time = time.time()
        diff = loop_time - start
        for key in cache.copy():
            data = cache[key]
            if diff >= data:
                del cache[key]
    return cache
print(session(cache,5))



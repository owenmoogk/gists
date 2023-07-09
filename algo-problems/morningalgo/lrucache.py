cache = []

def addToCache(data):
    if len(cache) > 3:
        cache.insert(0,data)
        cache.pop()
from queue import PriorityQueue
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    cache_dict = {city.lower():False for city in cities}
    if cacheSize==0:
        answer = 5*len(cities)
        return answer
    for city in cities:
        city = city.lower()
        # cache miss
        if cache_dict[city]==False:
            if len(cache)>=cacheSize:
                least_recently_used_city = cache.popleft()
                cache_dict[least_recently_used_city] = False
            cache.append(city)
            cache_dict[city] = True
            answer+=5
        # cache hit(is in the cache deque)
        else:
            cache.remove(city)
            cache.append(city)
            answer+=1
    return answer
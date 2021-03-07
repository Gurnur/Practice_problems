"""
Whenever you expose a web service / api endpoint, you need to implement a rate 
limiter to prevent abuse of the service (DOS attacks).

Implement a RateLimiter Class with an isAllow method. Every request comes in with 
a unique clientID, deny a request if that client has made more than 100 requests 
in the past second.
"""
from collections import deque
from collections import defaultdict

class RateLimiter():
    """
        Approach: Leaky/Token Bucket algorithm
        
        Initialize with 
        rate = no. of req/sec
        max_capacity = maximum no. of hits/ total bucket capacity
    """
    def __init__(self, rate, max_capacity):
        self.clients_rate = defaultdict(deque)
        self.rate = rate
        self.max_capacity = max_capacity

    """
        is_allowed returns if a request is allowed or not
        params: client_id and time of hit.
    """
    def is_allowed(self, client_id, timestamp):
        if client_id in self.clients_rate.keys():
            timings = self.clients_rate[client_id]
            while timings and int(timestamp) - int(timings[-1]) >= self.rate:
                timings.popleft()

            if len(timings) < self.max_capacity:
                timings.append(int(timestamp))
                return True
        else:
            self.clients_rate[client_id].append(timestamp)
            return True
    
        return False

# initialize the RateLimiter with rate (requests per second) and maximum hits/capacity.
obj = RateLimiter(1,3)
print(obj.is_allowed("abc", "1"))
print(obj.is_allowed("abc", "1"))
print(obj.is_allowed("abc", "1"))
print(obj.is_allowed("abc", "1"))
print(obj.is_allowed("bcd", "1"))   
print(obj.is_allowed("bcd", "1"))   
print(obj.is_allowed("bcd", "1"))   
print(obj.is_allowed("bcd", "1"))   
print(obj.is_allowed("cde", "1"))      



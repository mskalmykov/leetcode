from collections import deque

class RecentCounter:

    def __init__(self):
        self.d = deque()

    def ping(self, t: int) -> int:
        self.d.appendleft(t)

        while t - self.d[-1] > 3000:
            self.d.pop()
        
        return len(self.d)


obj = RecentCounter()
for i in [1, 100, 3001, 3002]:
    print(obj.ping(i))
    
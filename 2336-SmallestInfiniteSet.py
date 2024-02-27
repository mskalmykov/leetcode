import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.pq = []
        self.pq_set = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        if self.pq:
            ans = heapq.heappop(self.pq)
            self.pq_set.remove(ans)
        else:
            ans = self.smallest
            self.smallest += 1
        return ans
        
    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.pq_set:
            self.pq_set.add(num)
            heapq.heappush(self.pq, num)

        
obj = SmallestInfiniteSet()
obj.addBack(2)
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
obj.addBack(1)
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())


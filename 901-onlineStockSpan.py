class StockSpanner:

    def __init__(self):
        self.prices = []
        self.last = -1
        self.stack = []
        
    def next(self, price: int) -> int:
        self.prices.append(price)
        self.last += 1

        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()

        if self.stack:
            ans = self.last - self.stack[-1]
        else:
            ans = self.last + 1
        
        self.stack.append(self.last)

        return ans
        
obj = StockSpanner()
for p in [100, 80, 60, 70, 60, 75, 85]:
    print(obj.next(p))
print('---')
obj = StockSpanner()
for p in [31,41,48,59,79]:
    print(obj.next(p))
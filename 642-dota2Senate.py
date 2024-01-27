class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = senate
        l = len(q)
        start = {'D': 0, 'R': 0 }
        
        while True:
            banned = False
            for i in range(start[q[0]], l):
                if q[i] != q[0]:
                    q = q[:i] + q[i+1:]
                    l -= 1
                    banned = True
                    break
            if not banned:
                winner = q[0]
                break
            else:
                q = q[1:] + q[0]
                start[q[0]] = max(i - 2, 0)
        if winner == 'R':
            return 'Radiant'
        else:
            return 'Dire'
    
print(Solution().predictPartyVictory('RD'))
print(Solution().predictPartyVictory('RDD'))

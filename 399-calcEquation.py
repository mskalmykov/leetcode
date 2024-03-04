from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eq_tree = {}
        res = [-1] * len(queries)

        for i, (v1,v2) in enumerate(equations):
            if v1 in eq_tree:
                eq_tree[v1].append((v2, values[i]))
            else:
                eq_tree[v1] = [(v2, values[i])]

            if v2 in eq_tree:
                eq_tree[v2].append((v1, 1/values[i]))
            else:
                eq_tree[v2] = [(v1, 1/values[i])]

        for i, (q1, q2) in enumerate(queries):
            if (q1 not in eq_tree) or (q2 not in eq_tree):
                continue

            if q1 == q2:
                res[i] = 1
                continue

            seen = set()

            def dfs(node: str, q: str, k: float) -> float:
                if node in seen:
                    return -1
                else:
                    seen.add(node)
                    for child, val in eq_tree[node]:
                        if child == q:
                            return k * val
                        ret = dfs(child, q, k * val)
                        if ret != -1:
                            return ret
                    return -1
            
            res[i] = dfs(q1, q2, 1)

        return res
    
print(Solution().calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
print(Solution().calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
print(Solution().calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))

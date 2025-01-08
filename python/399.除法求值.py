#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from collections import defaultdict
# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        charsets = set()
        for a,b in equations:
            charsets.add(a)
            charsets.add(b)
        n = len(charsets)
        table = {v : i for i, v in enumerate(charsets)}
        tree = defaultdict(lambda: [0] * n)
        
        for v, i in table.items():
            tree[table[v]][i] = 1
        
        for i, (a, b) in enumerate(equations):
            ratio = values[i]
            
            tree[table[a]][table[b]] = ratio
            tree[table[b]][table[a]] = 1 / ratio
        
        def bfs(a, b):
            if a not in table or b not in table: return -1.0
            start, end = table[a], table[b]
            
            vis = set([start])
            queue = [(start, 1)]
            while queue:
                t = queue
                queue = []
                for node, v in t:
                    if tree[node][end] != 0: return tree[node][end] * v
                    
                    for i in range(n):
                        if i not in vis and tree[node][i] != 0:
                            vis.add(i)
                            queue.append((i, tree[node][i] * v))
                    
            return -1.0
        
        return [bfs(a,b) for a, b in queries]
# @lc code=end
#
# @lc app=leetcode.cn id=2940 lang=python3
#
# [2940] 找到 Alice 和 Bob 可以相遇的建筑
#
from collections import defaultdict
from math import inf
# @lc code=start
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n, qn = len(heights), len(queries)
        
        result = [-1] * qn
        qs = defaultdict(list)
        for qi, (a, b) in enumerate(queries):
            if a == b:
                result[qi] = a
                continue
            
            if a > b:
                a, b = b, a
            
            ah, bh = heights[a], heights[b]
            if ah < bh:
                result[qi] = b
            else:
                qs[b].append((ah, qi))
        
        alls = set()
        for num in heights:
            alls.add(num)
        alls = sorted(list(alls))
        table = {}
        i = 1
        for num in alls:
            if num not in table:
                table[num] = i
                i += 1
            
            table[num + 1] = i
            i += 1
            
        tn = table[alls[-1] + 1]
        tree = defaultdict(lambda : inf)
        
        def lowerbit(i):
            return i & (-i)
        
        def find(i):
            result = tree[i]
            while i <= tn:
                result = min(tree[i], result)
                i += lowerbit(i)
            return result if result != inf else -1

        def update(i, index):
            while i:
                tree[i] = min(tree[i], index)
                i -= lowerbit(i)
        
        for mi in range(n - 1, -1, -1):
            for h, qi in qs[mi]:
                r = find(table[h+1])
                result[qi] = r
            
            update(table[heights[mi]], mi)
        return result
# @lc code=end
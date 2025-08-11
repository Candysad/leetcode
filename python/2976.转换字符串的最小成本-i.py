#
# @lc app=leetcode.cn id=2976 lang=python3
#
# [2976] 转换字符串的最小成本 I
#
from collections import defaultdict
from math import inf
# @lc code=start
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dis = [[inf] * 26 for _ in range(26)]
        for  i in range(26):
            dis[i][i] = 0
        
        g = defaultdict(lambda : inf)
        for i, c in enumerate(original):
            a = ord(c) - ord('a')
            b = ord(changed[i]) - ord('a')
            w = cost[i]
            g[(a,b)] = min(g[(a,b)], w)
    
        for (a,b) in g:
            dis[a][b] = g[(a,b)]
        
        # Floyd
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        
        result = 0
        for i in range(len(source)):
            s = ord(source[i]) - ord('a')
            t = ord(target[i]) - ord('a')
            
            w = dis[s][t]
            if w == inf: return -1
            result += w
        
        return result

# @lc code=end
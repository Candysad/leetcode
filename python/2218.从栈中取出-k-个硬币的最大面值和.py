#
# @lc app=leetcode.cn id=2218 lang=python3
#
# [2218] 从栈中取出 K 个硬币的最大面值和
#
from functools import cache
# @lc code=start
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        @cache
        def dfs(i, k):
            if k == 0: return 0
            if i == n: return 0
            
            t = dfs(i+1, k)
            
            pre = 0
            for j in range(k):
                if j == len(piles[i]): break
                
                pre += piles[i][j]
                t = max(t, pre + dfs(i+1, k-j-1))
            return t
        
        return dfs(0, k)
# @lc code=end
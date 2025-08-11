#
# @lc app=leetcode.cn id=1416 lang=python3
#
# [1416] 恢复数组
#
from functools import cache
# @lc code=start
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        @cache
        def dfs(i):
            if i == n: return 1
            if s[i] == '0': return 0
            
            now = int(s[i])
            t = 0 
            while i < n and now <= k:
                t += dfs(i+1)
                i += 1
                if i < n:
                    now = now * 10 + int(s[i])
                
            return t % mod

        return dfs(0)
# @lc code=end
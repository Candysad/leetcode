#
# @lc app=leetcode.cn id=2767 lang=python3
#
# [2767] 将字符串分割为最少的美丽子字符串
#
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        table = set([
                    '1',
                    '101',
                    '11001',
                    '1111101',
                    '1001110001',
                    '110000110101',
                    '11110100001001'])

        n = len(s)
        
        @cache
        def dfs(i):
            if i == n: return 0
            
            t = inf
            for j in range(i+1, n+1):
                if s[i:j] in table:
                    t = min(t, dfs(j))
            return t + 1
        
        result = dfs(0)
        return result if result != inf else -1     
# @lc code=end
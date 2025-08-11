#
# @lc app=leetcode.cn id=1220 lang=python3
#
# [1220] 统计元音字母序列的数目
#
from functools import cache
# @lc code=start
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        @cache
        def dfs(i, j):
            if i == n-1: return 1
            
            if j == 0: # a
                return (dfs(i+1, 1)) % mod
            
            elif j == 1: # e
                return (dfs(i+1, 0) + dfs(i+1, 2)) % mod
            
            elif j == 2: # i
                return (dfs(i+1, 0) + dfs(i+1, 1) + dfs(i+1, 3) + dfs(i+1, 4)) % mod
            
            elif j == 3: # o
                return (dfs(i+1, 2) + dfs(i+1, 4)) % mod
            
            else:
                return dfs(i+1, 0) % mod
        
        result = [dfs(0, i) for i in range(5)]
        return sum(result) % mod
# @lc code=end
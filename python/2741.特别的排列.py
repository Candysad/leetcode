#
# @lc app=leetcode.cn id=2741 lang=python3
#
# [2741] 特别的排列
#
from functools import cache
from collections import defaultdict
# @lc code=start
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        table = {num:i for i, num in enumerate(nums)}
        g = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    g[nums[i]].append(nums[j])
                    g[nums[j]].append(nums[i])

        @cache
        def dfs(stat, now):
            newstat = stat | (1 << table[now])
            if newstat == stat: return 0
            if newstat == 2**n - 1: return 1
            
            t = 0
            for nextnum in g[now]:
                t += dfs(newstat, nextnum)
            
            return t % mod
        
        result = 0
        for num in nums:
            result += dfs(0, num)
        return result % mod
# @lc code=end
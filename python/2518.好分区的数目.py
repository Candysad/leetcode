#
# @lc app=leetcode.cn id=2518 lang=python3
#
# [2518] 好分区的数目
#
from functools import cache
# @lc code=start
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        _sum = sum(nums)
        if _sum < 2 * k: return 0
        n = len(nums)
        
        @cache
        def dfs(i, pre):
            if pre >= k: return 0
            if i == n:
                if pre < k: return 1
                else: return 0
            
            return dfs(i+1, pre) + dfs(i+1, pre + nums[i])

        bads = 2 * dfs(0, 0)
        return (pow(2, n, mod) % mod - bads % mod) % mod
# @lc code=end
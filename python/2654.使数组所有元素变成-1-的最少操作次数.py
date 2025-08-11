#
# @lc app=leetcode.cn id=2654 lang=python3
#
# [2654] 使数组所有元素变成 1 的最少操作次数
#
from math import gcd, inf
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 in nums:
            return n - nums.count(1)
        
        result = inf
        for i in range(n):
            t = nums[i]
            for j in range(i+1, n):
                t = gcd(t, nums[j])
                if t == 1: result = min(j - i, result)
        
        if result == inf: return -1
        
        return result + n - 1 
# @lc code=end
#
# @lc app=leetcode.cn id=2875 lang=python3
#
# [2875] 无限数组的最短子数组
#
from itertools import accumulate
from math import inf
# @lc code=start
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        _sum = sum(nums)
        inner = target // _sum
        target %= _sum
        if target == 0: return inner * n
        
        pres = [0] + list(accumulate(nums))
        table = {pre:i for i, pre in enumerate(pres)}
        offset = 0
        result = inf
        for i in range(n-1, -1, -1):
            t = pres[i] - target
            if t in table:
                j = table[t]
                result = min(i-j, result)
            
            del table[pres[i]]
            offset += nums[i]
            table[-offset] = i - n
        if result == inf: return -1
             
        return result + inner * n
# @lc code=end
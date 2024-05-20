#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#
from math import inf
# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = sum(nums)
        
<<<<<<< HEAD
        
=======
        total_max = -inf
        total_min = inf
        premax = -inf
        premin = inf
        for n in nums:
            if premax < 0:
                premax = n
            else:
                premax += n
            total_max = max(total_max, premax)    
            
            
            if premin > 0:
                premin = n
            else:
                premin += n
            total_min = min(total_min, premin)
        
        if total_min == _sum:
            return total_max
        return max(total_max, _sum - total_min)
>>>>>>> 1f62bc645f6c39c2bf22ed1898eaccfa2d0381b9
# @lc code=end


#
# @lc app=leetcode.cn id=2817 lang=python3
#
# [2817] 限制条件下元素之间的最小绝对差
#
from bisect import bisect_left
from math import inf
# @lc code=start
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        pre = []
        n = len(nums)
        left, right = 0, x
        result = inf
        while right < n:
            i = bisect_left(pre, nums[left])
            pre.insert(i, nums[left])
            
            i = bisect_left(pre, nums[right])
            if i == len(pre):
                result = min(result, abs(nums[right] - pre[-1]))
            else:
                result = min(result, abs(nums[right] - pre[i]))
                if i > 0:
                    result = min(result, abs(nums[right] - pre[i-1]))
            
            if result == 0: return 0
            left += 1
            right += 1

        return result  
# @lc code=end
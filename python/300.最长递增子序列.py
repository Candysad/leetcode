#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        queue = [nums[0]]
        for num in nums[1:]:
            i = bisect_left(queue, num)
            if i == len(queue):
                queue.append(num)
            else:
                queue[i] = num
        
        return len(queue)
# @lc code=end
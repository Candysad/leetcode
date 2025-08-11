#
# @lc app=leetcode.cn id=2576 lang=python3
#
# [2576] 求出最多标记下标
#

# @lc code=start
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        for right in range((n+1) // 2, n):
            if nums[right] >= 2 * nums[left]:
                left += 1
        return 2 * left
# @lc code=end
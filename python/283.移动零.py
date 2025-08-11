#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0
        right = 0
        
        while right < n:
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1
        
        for i in range(left, n):
            nums[i] = 0
        
        return nums
# @lc code=end


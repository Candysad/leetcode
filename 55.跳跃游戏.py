#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        left = 0
        right= 0
        
        while right < n-1:
            if left > right:
                return False
            right = max(right, nums[left] + left)
            left += 1
        
        return True
# @lc code=end


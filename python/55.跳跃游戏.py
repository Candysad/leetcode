#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        now = 0
        end = nums[0]
        while now < n and now <= end:
            end = max(end, now + nums[now])
            now += 1
        
        if end < n - 1:
            return False
        return True
# @lc code=end


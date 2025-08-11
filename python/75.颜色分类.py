#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        left, right = 0, n-1
        now = 0
        
        while now <= right and left <= right:
            if nums[left] == 0:
                left += 1
            elif nums[right] == 2:
                right -= 1
            else:
                now = max(now, left)
                if nums[now] == 2:
                    nums[now], nums[right] = nums[right], nums[now]
                    right -= 1
                elif nums[now] == 0:
                    nums[now], nums[left] = nums[left], nums[now]
                    left += 1
                elif nums[now] == 1:
                    now += 1
# @lc code=end


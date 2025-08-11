#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        每次只看左右位置构成的长和较矮一端的高
        只需要更新矮的一边，从两头往中间遍历
        '''
        left = 0
        right = len(height) - 1
        max_volume = 0
        while left < right: 
            if height[left] < height[right]:
                volume = (right - left) * height[left]
                max_volume = volume if volume > max_volume else max_volume
                left += 1
            else:
                volume = (right - left) * height[right]
                max_volume = volume if volume > max_volume else max_volume
                right -= 1
        return max_volume                      
# @lc code=end


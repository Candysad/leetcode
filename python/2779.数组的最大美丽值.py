#
# @lc app=leetcode.cn id=2779 lang=python3
#
# [2779] 数组的最大美丽值
#
# @lc code=start
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        '''
        找子序列长度而非子序列具体内容，可以排序再找
        '''
        nums.sort()
        n = len(nums)
        result = 1
        left, right = 0, 0
        while right < n:
            if nums[right] - nums[left] <= 2 * k:
                right += 1
                result = max(result, right - left)
            else:
                left += 1   
        return result
# @lc code=end
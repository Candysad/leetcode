#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            print(left, right)
            mid = left + ((right - left) >> 1)
            if nums[mid] == target: return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left
# @lc code=end
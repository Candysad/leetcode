#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[0] <= nums[mid]: # 左侧[0...mid]有序
                if nums[0] <= target < nums[mid]: # 目标在左侧
                    right = mid - 1
                else: # 目标不在左侧，要么比nums[0] 还小，要么比 nums[mid] 大
                    left = mid + 1
            
            else: # [0...mid] 里有断开的位置，那至少右侧是有序的
                if nums[mid] < target <= nums[n-1]: # mid 在右侧里面
                    left = mid + 1
                else: # mid 不在右侧里面
                    right = mid - 1
        
        return -1
# @lc code=end


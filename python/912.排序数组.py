#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
from random import randint
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        def quick(start, end):
            if start >= end: return
            
            p = randint(start, end)
            nums[start], nums[p] = nums[p], nums[start]
            p = nums[start]
            
            left, mid, right = start, start+1, end+1
            while mid < right:
                if nums[mid] > p:
                    nums[mid], nums[right-1] = nums[right-1], nums[mid]
                    right -=1
                elif nums[mid] < p:
                    nums[mid], nums[left+1] = nums[left+1], nums[mid]
                    left += 1
                    mid += 1
                else:
                    mid += 1
            nums[left], nums[start] = nums[start], nums[left]

            quick(start, left-1)
            quick(right, end)
            
        quick(0, n-1)
        return nums
# @lc code=end
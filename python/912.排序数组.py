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
        
        def sift_down(start, end):
            item = nums[start]
            
            p = start
            c = 2 * p + 1
            while c <= end:
                cr = c + 1
                if cr <= end and nums[cr] > nums[c]:
                    c = cr
                
                if nums[c] > item:
                    nums[p] = nums[c]
                    p = c
                    c = 2 * p + 1
                else:
                    break
            nums[p] = item
        
        for i in range((n-2) >> 1, -1, -1):
            sift_down(i, n-1)
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            sift_down(0, i-1)
        return nums
# @lc code=end
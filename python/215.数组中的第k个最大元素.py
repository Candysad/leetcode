#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from random import randint
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
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
        
        for i in range((n-2)>>1, -1, -1):
            sift_down(i, n-1)
        
        for i in range(1, k):
            nums[0], nums[-i] = nums[-i], nums[0]
            sift_down(0, n-i-1)
        return nums[0]
# @lc code=end
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
        
        def quick(start, end, k):   
            p = randint(start, end)
            nums[start], nums[p] = nums[p], nums[start]
            p = nums[start]
            
            left, mid, right = start, start+1, end+1
            while mid < right:
                if nums[mid] > p:
                    nums[mid], nums[right-1] = nums[right-1], nums[mid]
                    right -= 1
                elif nums[mid] < p:
                    nums[mid], nums[left+1] = nums[left+1], nums[mid]
                    mid += 1
                    left += 1
                else:
                    mid += 1
            nums[start], nums[left] = nums[left], nums[start]
            
            rightlen = end - right + 1
            if rightlen >= k:
                return quick(right, end, k)
            
            leftlen = end - left + 1
            if leftlen >= k:
                return p
            
            return quick(start, left-1, k-leftlen)
            
        return quick(0, n-1, k)    
# @lc code=end
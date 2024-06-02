#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from random import randint
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        三路快速排序
        '''
        def quick(start, end, k):
            p = randint(start, end)
            nums[start], nums[p] = nums[p], nums[start]
            p = nums[start]
            
            left, mid, right = start, start+1, end+1
            while mid < right:
                if nums[mid] > p:
                    nums[mid], nums[right-1] = nums[right-1], nums[mid]
                    right-=1
                elif nums[mid] < p:
                    nums[left+1], nums[mid] = nums[mid], nums[left+1]
                    left += 1
                    mid += 1
                else:
                    mid += 1
            nums[start], nums[left] = nums[left], nums[start]
            
            rightlength = end - right + 1
            if rightlength >= k:
                return quick(right, end)
            else:
                leftlength = end - left + 1
                if leftlength >= k:
                    return p
                else:
                    return quick(start, left-1, k-leftlength)
        
        return quick(0, len(nums)-1, k)
            
        
        

# @lc code=end


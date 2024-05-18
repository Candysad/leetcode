#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        二分
        '''
        n = len(nums)
        if n == 1:
            return 0
        
        def check(i):
            if i == 0:
                if nums[0] > nums[1]:
                    return 2 # 峰值
                else:
                    return 1 # 向右递增
            if i == n-1:
                if nums[-1] > nums[-2]:
                    return 2
                else:return -1 # 向左递增
            
            else:
                if nums[i-1] < nums[i] > nums[i+1]:
                    return 2
                
                if nums[i-1] < nums[i] < nums[i+1]:
                    return 1
                
                if nums[i-1] > nums[i] > nums[i+1]:
                    return -1
                
                if nums[i-1] > nums[i] < nums[i+1]:
                    return 0 # 谷底
        
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            c = check(mid)
            
            if c == 2:
                return mid
            
            if c == 1 or c == 0: # 谷底或向右递增
                left = mid + 1
            if c == -1: # 向左递增
                right = mid - 1

            
        
# @lc code=end


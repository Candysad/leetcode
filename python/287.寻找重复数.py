#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def check(target):
            result = 0
            for n in nums:
                if n < target:
                    result += 1
            return result
        
        n = len(nums) - 1
        left, right = 1, n
        while left < right-1:
            mid = (left + right) // 2
            c = check(mid)
            if c <= mid-1:
                left = mid
            else:
                right = mid 
        return right if check(right) <= right - 1 else left
# @lc code=end
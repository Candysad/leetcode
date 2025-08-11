#
# @lc app=leetcode.cn id=2601 lang=python3
#
# [2601] 质数减法运算
#
from bisect import bisect_left
# @lc code=start
pri = []
n = 1009
not_prime = [False] * (n+1)

for i in range(2, n + 1):
    if not not_prime[i]:
        pri.append(i)
    for pri_j in pri:
        if i * pri_j > n:
            break
        not_prime[i * pri_j] = True
        if i % pri_j == 0:
            break
pri = [0] + pri
np = len(pri)

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        nums = [0] + nums
        # def bisect(i):
        #     target = nums[i] - nums[i-1] - 1
        #     if target < 0:
        #         return False
            
        #     left, right = 0, np-1
        #     while left < right-1:
        #         mid = (left + right) // 2
        #         c = pri[mid]
        #         if c == target:
        #             left = mid
        #             break
        #         elif c < target:
        #             left = mid
        #         else:
        #             right = mid

        #     nums[i] -=  pri[left]
        #     return True
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
            
            target = nums[i] - nums[i-1] - 1
            j = bisect_left(pri, target)    
            if pri[j] == target:
                nums[i] = nums[i-1] + 1
            elif j == 0:
                return False
            else:
                nums[i] -= pri[j-1]
        
        return True

# @lc code=end


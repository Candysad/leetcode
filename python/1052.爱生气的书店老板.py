#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        left, right = 0, 0
        total_sum = 0
        while right < minutes:
            total_sum += customers[right]
            right += 1
        
        for i in range(right, n):
            total_sum += 0 if grumpy[i] else customers[i]
            
        
        result = total_sum
        while right < n:
            total_sum -= customers[left] if grumpy[left] else 0
            left += 1
            
            total_sum += customers[right] if grumpy[right] else 0
            right += 1
            
            result = max(total_sum, result)
        
        return result
        
# @lc code=end


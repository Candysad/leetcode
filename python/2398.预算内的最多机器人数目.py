#
# @lc app=leetcode.cn id=2398 lang=python3
#
# [2398] 预算内的最多机器人数目
#
from collections import deque
# @lc code=start
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        maxs = deque()
        left, right = 0, 0
        now_sum = 0
        result = 0
        while right < n:
            charge, run = chargeTimes[right], runningCosts[right]
            while maxs and maxs[-1] < charge:
                maxs.pop()
            maxs.append(charge)
            now_sum += run
            right += 1
            
            b = maxs[0] + (right - left) * now_sum
            while b > budget:
                charge, run = chargeTimes[left], runningCosts[left]
                if charge == maxs[0]:
                    maxs.popleft()
                now_sum -= run
                left += 1
                
                b = maxs[0] + (right - left + 1) * now_sum if maxs else 0
            
            result = max(right - left, result)
        
        return result
# @lc code=end
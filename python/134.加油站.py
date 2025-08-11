#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from functools import cache
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        
        n = len(gas)
        for i in range(n):
            if gas[i] >= cost[i]:
                start, now, pre = i, (i+1) % n, gas[i] - cost[i]
                break
        
        while now != start:
            new = pre + gas[now] - cost[now]
            if new < 0:
                for i in range(now, n):
                    if gas[i] >= cost[i]:
                        start, now, pre = i, (i+1) % n, gas[i] - cost[i]
                        break
                
            else:
                now = (now + 1) % n
                pre = new
        return start
# @lc code=end


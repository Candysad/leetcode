#
# @lc app=leetcode.cn id=2332 lang=python3
#
# [2332] 坐上公交的最晚时间
#

# @lc code=start
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        
        result = passengers[0] - 1 
        nb, np = len(buses), len(passengers)
        bi, pi = 0, 0
        while bi < nb and pi < np:
            ct = 0
            for t in range(capacity):
                if passengers[pi] <= buses[bi]:
                    if pi > 0 and passengers[pi] != passengers[pi-1] + 1:
                        result = max(result, passengers[pi] - 1)
                    pi += 1
                    ct += 1
                else: break
            if ct < capacity:
                if buses[bi] != passengers[pi-1]:
                    result = max(result, buses[bi])
            bi += 1
        return result
# @lc code=end
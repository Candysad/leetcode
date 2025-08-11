#
# @lc app=leetcode.cn id=2105 lang=python3
#
# [2105] 给植物浇水 II
#

# @lc code=start
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        if n == 1:
            return 0 
        a, b = 0, n - 1
        ca, cb = capacityA, capacityB
        result = 0
        while a < b:
            if ca >= plants[a]:
                ca -= plants[a]
            else:
                ca = capacityA - plants[a]
                result += 1
                
            if cb >= plants[b]:
                cb -= plants[b]
            else:
                cb = capacityB - plants[b]
                result += 1
            a += 1
            b -= 1
        
        if a == b:
            if ca >= cb:
                if ca < plants[a]:
                    result += 1
            else:
                if cb < plants[b]:
                    result += 1
        return result       
# @lc code=end


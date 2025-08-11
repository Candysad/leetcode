#
# @lc app=leetcode.cn id=2079 lang=python3
#
# [2079] 给植物浇水
#

# @lc code=start
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 0
        reset = capacity
        for i, p in enumerate(plants):
            if capacity >= p:
                result += 1
                capacity -= p
            else:
                result += 2*i + 1
                capacity = reset - p
        return result
# @lc code=end


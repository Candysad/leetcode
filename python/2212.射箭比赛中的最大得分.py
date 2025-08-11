#
# @lc app=leetcode.cn id=2212 lang=python3
#
# [2212] 射箭比赛中的最大得分
#
from functools import cache
# @lc code=start
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        result = None
        t = 0
        
        path = [0] * 12
        def dfs(i, nums):
            if i == 12:
                nonlocal t, result
                _sum = sum(path)
                if _sum > t:
                    t = _sum
                    result = path.copy()
                return 
            
            if nums > aliceArrows[i]:
                path[i] = i
                dfs(i+1, nums - aliceArrows[i] - 1)
                path[i] = 0
            
            dfs(i+1, nums)
        
        dfs(1, numArrows)
        
        t = [0] * 12
        for i in range(11, -1, -1):
            if result[i]:
                a = aliceArrows[i] + 1
                numArrows -= a
                t[i] = a
        t[0] = numArrows
        return t
# @lc code=end
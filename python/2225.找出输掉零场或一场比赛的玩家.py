#
# @lc app=leetcode.cn id=2225 lang=python3
#
# [2225] 找出输掉零场或一场比赛的玩家
#
from collections import defaultdict
# @lc code=start
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        result = [[], []]
        degree = defaultdict(int)
        
        for a, b in matches:
            degree[a] += 0
            degree[b] += 1
        
        for key in degree:
            if degree[key] < 2:
                result[degree[key]].append(key)
        
        result[0].sort()
        result[1].sort()
        return result
# @lc code=end
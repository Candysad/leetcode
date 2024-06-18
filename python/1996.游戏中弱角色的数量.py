#
# @lc app=leetcode.cn id=1996 lang=python3
#
# [1996] 游戏中弱角色的数量
#
from collections import defaultdict
# @lc code=start
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:x[0])
        
        
        m1, m2 = properties[-1][0], 0
        result = 0
        for v1, v2 in properties[::-1]:
            t = m2
            if m1 != v1:
                m2 = t
                m1 = v1
            if m2 > v2: result += 1
            t = max(t, v2)
        return result
# @lc code=end


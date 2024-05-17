#
# @lc app=leetcode.cn id=2244 lang=python3
#
# [2244] 完成所有任务需要的最少轮数
#
from math import inf
from functools import cache
from collections import Counter
# @lc code=start
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        def resolve(i):
            if i == 1:
                return -1
            
            if i == 2:
                return 1
                
            if i % 3 == 0:
                return i // 3
            
            if i % 3 == 1:
                return (i - 4) // 3 + 2
            if i % 3 == 2:
                return i // 3 + 1
        
        counter = Counter(tasks)
        result = 0
        for v in counter.values():
            t = resolve(v)
            if t == -1:
                return -1
            
            result += t
        return result     
# @lc code=end


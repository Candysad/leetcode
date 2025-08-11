#
# @lc app=leetcode.cn id=1792 lang=python3
#
# [1792] 最大平均通过率
#
from heapq import *
# @lc code=start
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        if len(classes) == 1:
            return (classes[0] + extraStudents) / (classes[1] + extraStudents)
        
        _sum = 0
        queue = []
        for p, t in classes:
            _sum += p / t
            if p < t:
                heappush(queue, (-(t-p)/(t*(t+1)), p, t))
        
        while extraStudents and queue:
            ratio, p, t = queue[0]
            _sum += -ratio
            p += 1
            t += 1
            ratio = -(t-p)/(t*(t+1))
            
            heapreplace(queue, (ratio, p, t))
            extraStudents -= 1
        
        return _sum / len(classes)  
# @lc code=end


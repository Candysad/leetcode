#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        result = [-1] * n
        
        for p in people:
            index = -1
            for i in range(n):
                if result[i] == -1:
                    index += 1
                if index == p[1]:
                    result[i] = p
                    break
        
        return result
# @lc code=end


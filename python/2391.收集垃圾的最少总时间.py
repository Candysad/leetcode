#
# @lc app=leetcode.cn id=2391 lang=python3
#
# [2391] 收集垃圾的最少总时间
#

# @lc code=start
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        gi, pi, mi = 0, 0, 0
        result = len(garbage[0])
        travel = [0] + travel
        for i in range(1, len(travel)):
            travel[i] += travel[i-1]
            s = set([c for c in garbage[i]]) 
            result += len(garbage[i])
            if 'M' in s:
                result += travel[i] - travel[mi]
                mi = i
            if 'P' in s:
                result += travel[i] - travel[pi]
                pi = i
            if 'G' in s:
                result += travel[i] - travel[gi]
                gi = i
        return result
# @lc code=end


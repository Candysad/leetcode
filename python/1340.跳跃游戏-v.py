#
# @lc app=leetcode.cn id=1340 lang=python3
#
# [1340] 跳跃游戏 V
#
from functools import cache
# @lc code=start
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        
        @cache
        def dfs(i):
            t = 0
            # 左
            for j in range(i-1, max(0, i-d) - 1, -1):
                if arr[j] >= arr[i]:
                    break
                t = max(t, dfs(j))
            
            # 右
            for j in range(i+1, min(n, i+d+1)):
                if arr[j] >= arr[i]:
                    break
                t = max(t, dfs(j))
            
            return t + 1

        result = 0
        for i in range(n):
            result = max(result, dfs(i))
        return result   
# @lc code=end
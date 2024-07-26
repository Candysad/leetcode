#
# @lc app=leetcode.cn id=1043 lang=python3
#
# [1043] 分隔数组以得到最大和
#
from functools import cache
# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @cache
        def dfs(i, lens, premax):
            if i == n: 
                return premax * lens
            
            if lens == k:
                return lens * premax + dfs(i + 1, 1, arr[i])
            
            t1 = dfs(i+1, lens+1, max(premax, arr[i]))
            t2 = lens * premax + dfs(i+1, 1, arr[i])
            return max(t1, t2)
        
        return dfs(0, 0, 0)
# @lc code=end
#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0
        def dfs(i, cs, lc, rc):
            if i == n:
                nonlocal result
                result += 1
            
            now = cs | lc | rc
            for j in range(n):
                if ((now >> j) & 1) == 0:
                    tcs = cs | (1 << j)
                    tl = (lc << 1) | (1 << (j+1))
                    tr = (rc >> 1) | ((1 << (j-1)) if j > 0 else 0)
                    
                    dfs(i+1, tcs, tl, tr)
                    
        dfs(0, 0, 0, 0)
        return result
# @lc code=end
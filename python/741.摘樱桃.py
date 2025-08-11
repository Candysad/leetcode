#
# @lc app=leetcode.cn id=741 lang=python3
#
# [741] 摘樱桃
#
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        @cache
        def dfs(k, ix, jx):
            if k == 0:
                return grid[0][0]
            # 不能越界
            if ix < 0 or jx < 0 or k < ix or k < jx:
                return -inf
            # 不可达
            if grid[ix][k-ix] == -1 or grid[jx][k-jx] == -1:
                return -inf
            
            last = max(dfs(k-1, ix, jx), dfs(k-1, ix-1, jx-1), dfs(k-1, ix, jx-1), dfs(k-1, ix-1, jx))
            last += grid[ix][k-ix] + grid[jx][k-jx] if ix != jx else grid[ix][k-ix]
            return last
        
        return max(dfs(2*n-2, n-1, n-1), 0)
        
        # n = len(grid)
        # # if n == 1:
        # #     return 1 if grid[0][0] == 1 else 0
        
        # # 一次遍历把两趟的都拿了
        # # 一边最多走 n-1 步，总共最多 2*n-2 步
        # dp = [[[-inf] * (n+1) for _ in range(n+1)] for __ in range(2*n-1)]
        # dp[0][1][1] = grid[0][0]
        
        # #  走了 k 步，一个横坐标为 i， 另一个为 j，纵坐标为 k-i 和 k-j
        # for k in range(1, 2 * n - 1):
        #     # 一边最多走 n-1 步,多出来的只能是另一边走的
        #     for ix in range(max(0, k-n+1), min(k, n-1)+1):
        #         iy = k - ix
        #         if grid[ix][iy] == -1:
        #             continue
        #         # 不用完全遍历，不然就算入了完全相同的组合
        #         for jx in range(ix, min(k, n-1)+1):
        #             jy = k - jx
        #             if grid[jx][jy] == -1:
        #                 continue

        #             # 上一步过来的情况
        #             # 都右，都下，一下一右，一右一下
        #             dp[k][ix + 1][jx + 1] = max(dp[k-1][ix+1][jx+1], dp[k-1][ix][jx], dp[k-1][ix][jx+1], dp[k-1][ix+1][jx])
        #             dp[k][ix + 1][jx + 1] += grid[ix][iy] + grid[jx][jy] if ix != jx else grid[ix][iy]

        # return max(dp[-1][-1][-1], 0)
# @lc code=end


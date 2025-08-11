#
# @lc app=leetcode.cn id=1463 lang=python3
#
# [1463] 摘樱桃 II
#

# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0] * m for _ in range(m)] for __ in range(n+1)]
        # i 左边那个离左边界的距离
        # j 右边那个离右边界的距离
        # m-1-j == i 时在同一个位置
        for k in range(1, n+1):
            # 最开始几行到不了中间
            for i in range(min(m, k)):
                for j in range(min(m,k)):
                    # 从上一行的情况过来
                    # 左中右 * 左中右九种情况，去除越界的
                    
                    lasts = [0]
                    for ilast, jlast in [
                        (i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1), (i, j), (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1),
                        ]:
                        if 0 <= ilast < m and 0 <= jlast < m:
                            if dp[k-1][ilast][jlast]:
                                lasts.append(dp[k-1][ilast][jlast])
                    dp[k][i][j] = max(lasts)
                    dp[k][i][j] += grid[k-1][i] + grid[k-1][m-1-j] if m-1-j != i else grid[k-1][i]
        result = []
        for t in dp[-1]:
            result.extend(t)
        # print(result)
        return max(result)
  
# @lc code=end


#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        数学题+DP
        容易想到DP的状态
        怎么设计dp转移
        当前值为以当前点为右下角的最大正方形的边长
        由←↖↑三个方向值决定
            当前如果是0就直接不是正方形
            当前是1
               ←↑都是正方形和当前位置结合能增长边长1个格子
               ↖也影响实际长度，即新正方形内部的实心的部分
            结合画图
                三个方向最小的决定下一个
                三个方向有0则说明不能用之前的，当前就还是1（自己一个形成正方形）
        上左两边缘单独判断
        '''
        m = len(matrix)
        n = len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        result = 0
        for i in range(0, m):
            for j in range(0, n):
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                result = max(result, dp[i][j])
        return result * result
# @lc code=end


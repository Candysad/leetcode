#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        动态规划
        带特殊权重的 62.
        '''
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        t = [0 for _ in range(n)]
        for j in range(n):
            if obstacleGrid[0][j]:
                break
            t[j] = 1 
        # print(t)
        for i in range(1, m):
            # 每行的开头单独分析要不要处理
            if obstacleGrid[i][0]:
                t[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    t[j] = 0
                    continue
                t[j] += t[j-1]
            # print(t)
        
        return t[-1]    
# @lc code=end


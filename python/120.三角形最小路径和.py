#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        layer = len(triangle)
        dp = triangle[-1].copy()
        
        for i in range(layer-2, -1, -1): # 从倒数第2层开始
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
        
        
        '''
        有诡异形状的矩阵二维DP
        三角形两头都要单独处理
        
        从上到下
        '''
        # layers = len(triangle)
        # if layers == 1:
        #     return triangle[0][0]
        
        # for i in range(1, layers-1): # 从 0 开始数，从第 2 层到到倒数第二层
        #     triangle[i][0]  += triangle[i-1][0] # 每层第1个
        #     triangle[i][-1] += triangle[i-1][-1] # 每层最后个
        #     for j in range(1, i):
        #         triangle[i][j]+= min(triangle[i-1][j-1], triangle[i-1][j])
        
        # # 最后一层单独处理，顺便把最小的找到
        # triangle[-1][0]  += triangle[-2][0]
        # triangle[-1][-1] += triangle[-2][-1]
        # result = triangle[-1][0]
        # for j in range(1, layers-1):
        #     result = min(result, triangle[-1][j] + min(triangle[-2][j-1], triangle[-2][j]))   
        # return min(result, triangle[-1][-1])
        
        '''
        从下到上
        不需要处理两端
        更简洁
        '''
        # layers = len(triangle)
        # if layers == 1:
        #     return triangle[0][0]
        
        # for i in range(layers-2, 0, -1):
        #     for j in range(i + 1):
        #         triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        
        # return triangle[0][0] + min(triangle[1][0], triangle[1][1])
                
        
# @lc code=end


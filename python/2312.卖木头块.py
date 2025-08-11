#
# @lc app=leetcode.cn id=2312 lang=python3
#
# [2312] 卖木头块
#

# @lc code=start
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        '''
        动态规划
        最朴素：
        每次在新的各自根据之前的最佳确定当前的最佳
        最开始由prices确定每个格子左上方区域最小可行的钱
        （直接用每个prices确定一个格子的可能的钱
        转移时在格子内按横纵分别转移，看内部有没有更好的情况
        
        方法题
        最朴素的动态规划需要想到状态设计的基础上想到如何确定初始状态和转移过程
        '''
        # price中的大小直接对应下标
        dp = [[0]*(n+1) for _ in range(m+1)]
        for x, y , price in prices:
            dp[x][y] = price
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(i):
                    dp[i][j] = max(dp[i][j], dp[i-k][j] + dp[k][j]) # 用k找内部横纵最佳
                for k in range(j):
                    dp[i][j] = max(dp[i][j], dp[i][j-k] + dp[i][k])
        return dp[-1][-1]
        
        '''
        官方题解的记忆化搜索和递归其实就是动态规划的本质
        相当于两者本质思路一致，代码设计顺序相反
        官方题解会超时...😓
        '''
        # value = dict()
        # @cache
        # def dfs(x: int, y: int) -> int:
        #     ret = value.get((x, y), 0)

        #     if x > 1:
        #         for i in range(1, x):
        #             ret = max(ret, dfs(i, y) + dfs(x - i, y))
            
        #     if y > 1:
        #         for j in range(1, y):
        #             ret = max(ret, dfs(x, j) + dfs(x, y - j))
            
        #     return ret
        
        # for (h, w, price) in prices:
        #     value[(h, w)] = price
        
        # ans = dfs(m, n)
        # dfs.cache_clear()
        # return ans
# @lc code=end


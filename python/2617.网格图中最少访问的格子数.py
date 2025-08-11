#
# @lc app=leetcode.cn id=2617 lang=python3
#
# [2617] 网格图中最少访问的格子数
#

# @lc code=start
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        ''''
        动态规划
        每个格子横竖分别更新距离k以内的格子
        会超时..😓
        方向是对的
        但是从前往后的维护过程有不必要的遍历（不是最优解但是还是遍历了）
        
        O(mn(m+n))
        O(mn)
        '''
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[-1]* (n) for _ in range(m)]
        # dp[0][0] = 0
        
        # for i in range(m):
        #     for j in range(n):
        #         if dp[i][j] == -1:
        #             continue
        #         # 横着
        #         k = j + 1
        #         while k < n and k <= grid[i][j] + j:
        #             dp[i][k] = dp[i][j] + 1 if dp[i][k] == -1 else min(dp[i][k], dp[i][j] + 1)
        #             k += 1
                
        #         # 竖着
        #         k = i + 1
        #         while k < m and k <= grid[i][j] + i:
        #             dp[k][j] = dp[i][j] + 1 if dp[k][j] == -1 else min(dp[k][j], dp[i][j] + 1)
        #             k += 1
        
        # for line in dp:
        #     print(line)
        
        # return -1 if dp[-1][-1] == -1 else dp[-1][-1] + 1
        
        ''''
        优先队列 优化数组的维护过程
        把前面的存起来
        取前面最小步数的格子给当前格子用
        如果没有符合的格子了说明当前格子不可到达(后面更远的就更不可到达了)
        通过优先队列和优先配合丢弃不可到达的部分减少后续遍历
        维护过程从前往后
        但是从每个格子往之前的位置看，而不是每个格子往后面没看过的地方看
        '''
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]* (n) for _ in range(m)]
        dp[0][0] = 1
        
        # 按行列保存
        pqr = [[] for _ in range(m)]
        pqc = [[] for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                # 取当前行满足条件的最小格子
                # 可以扔掉前面过不来的的因为后面遍历的格子只会比现在的更远
                while pqr[i] and grid[i][pqr[i][0][1]] + pqr[i][0][1] < j: # j 是当前的 k
                                                                           # pqr[0]是当前行之前走过来步数小的格子
                    heappop(pqr[i]) # 当前步数最小的格子过不来，就丢弃
                if pqr[i]: # 还有过的来的,则取当前行最小的走一步
                    dp[i][j] = dp[i][pqr[i][0][1]] + 1 if dp[i][j] == -1 else min(dp[i][j], dp[i][pqr[i][0][1]] + 1)
                
                # 列
                while pqc[j] and grid[pqc[j][0][1]][j] + pqc[j][0][1] < i:
                    heappop(pqc[j])
                if pqc[j]:
                    dp[i][j] = dp[pqc[j][0][1]][j] + 1 if dp[i][j] == -1 else min(dp[i][j], dp[pqc[j][0][1]][j] + 1)
                    
                if dp[i][j] != -1: #当前点可达
                    heappush(pqr[i], (dp[i][j], j))
                    heappush(pqc[j], (dp[i][j], i))
                    
        return dp[-1][-1]
# @lc code=end


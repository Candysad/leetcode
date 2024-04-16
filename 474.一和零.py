#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        0-1 背包
        每个coin的面值都是1，但是每个容量不同
        不同组合不算不同答案
        两种容量分别影响
        
        将递归改成dp
        由递归可以看出状态只和 i m n有关，他们相互又是无关的
        所以 dp[i][j][k] 
        表示遍历至第i个
        且（选用i或不选后）已经用了 j 个 0 和 k 个 1 时的最多选用个数
        
        c0, c1 = strs[i] 中0和1的个数
        dp[i][j][k] = max(
            dp[i-1][j-c0][k-c1] + 1, # 选i
            dp[i-1][j][k] # 不选
        )
        
        初始dp[0] 全为 0 即可
        
        dp转移比递归慢....
        '''
        t = len(strs)
        dp = [[[0]*(n+1) for _ in range(m+1)] for __ in range(t+1)]
        
        for i in range(1, t+1):
            s = strs[i-1]
            c0 = s.count('0')
            c1 = s.count('1')
            # 不选 i
            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i-1][j][k]
            
            # 选 i
            for j in range(c0, m+1):
                for k in range(c1, n+1):
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-c0][k-c1] + 1)
        
        return dp[-1][-1][-1]

        '''
        递归会超时
        加上@cache就通过了
        '''
        # c0 = [s.count('0') for s in strs]
        # c1 = [s.count('1') for s in strs]
        # l = len(strs)
        
        # @cache
        # def dfs(i, m, n):
        #     nonlocal l
        #     if i == l:
        #         return 0
            
        #     # 放入当前
        #     t1 = 0
        #     if c0[i] <= m and c1[i] <= n:
        #         t1 = 1 + dfs(i+1, m-c0[i], n-c1[i])
            
        #     # 不放入
        #     t2 = dfs(i+1, m, n)
            
        #     return max(t1, t2)

        # return dfs(0, m, n)

# @lc code=end


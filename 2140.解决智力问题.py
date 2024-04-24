#
# @lc app=leetcode.cn id=2140 lang=python3
#
# [2140] 解决智力问题
#

# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        '''
        冻结期不同的买股票（不用买卖直接赚钱）
        递归想
        '''
        # n = len(questions)
        # if n == 1:
        #     return questions[0][0]
        
        # @cache
        # def dfs(i):
        #     nonlocal n
        #     if i >= n:
        #         return 0  

        #     # 今天不买
        #     t1 = dfs(i+1)
            
        #     # 今天买
        #     t2 = dfs(i+questions[i][1]+1)
            
        #     return max(t1, t2+questions[i][0])
        
        # return dfs(0)
        
        '''
        改成DP
        观察递归可以看出，每天的状态由两种情况组成
        1. 昨天没买顺位到今天
        2. 很早之前买了跳到今天
        
        所以不是同一时刻完成转移，而是两次比较实现转移
        dp[i] 表示能得到的最大收益
        
        '''
        n = len(questions)
        if n == 1:
            return questions[0][0]
        
        dp = [0] * n
        for i in range(n):
            skip = questions[i][1]
            
            # 今天不买，更新明天
            if i < n-1:
                dp[i+1] = max(dp[i+1], dp[i])
            
            # 今天买，跳到后面更新
            dp[i] += questions[i][0] # 此处更新了今天的值，变为今天已买
            nextday = skip + i + 1
            if nextday < n:
                dp[nextday] = max(dp[nextday], dp[i])
        
        return max(dp) 
# @lc code=end


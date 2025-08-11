#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][i] = 1
        
        for i in range(n, 0, -1): # 回文左侧要从大到小遍历，以保证里面的部分之前遍历过了
            left = s[i-1]
            for j in range(i+1, n+1):
                right = s[j-1]
                
                if i == j - 1 and left == right:
                    dp[i][j] = 1
                
                elif left == right and dp[i+1][j-1]:
                    dp[i][j] = 1
        
        spans = [[] for _ in range(n)]
        for i in range(1,n+1):
            for j in range(i, n+1):
                if dp[i][j]:
                    spans[i-1].append(j-1)
        
        pre = []
        result = []
        def dfs(left):
            if left == n:
                result.append(pre.copy())
                return
            for right in spans[left]:
                pre.append(s[left:right+1])
                dfs(right+1)
                pre.pop()
        dfs(0)
        return result
# @lc code=end


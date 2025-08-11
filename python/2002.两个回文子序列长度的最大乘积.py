#
# @lc app=leetcode.cn id=2002 lang=python3
#
# [2002] 两个回文子序列长度的最大乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        
        # 二进制存每种选择情况对应的最长回文子序列长度
        # 从全不选 000...000 到全选 111...111
        dp = [0] * (1 << n)
        
        for i in range(n): # i 高位，j 低位
            dp[1 << i] = 1
            for j in range(i-1, -1, -1): # 遍历每个一前一后的位置
                if s[i] == s[j]: # 两端可以形成回文
                    # 进去找内部最长
                    # 内部每种情况的状态都可以加上两端
                    # 内部全不选是 0...100...001...0 去除两端中间即是全 0
                    # 内部全选是   0...111...111...0 即中间是 1 << (i-j-1) << (j+1)
                    # 先算出内部的值，再挪过去
                    for k in range(1 << (i - j - 1)):
                        dp[k << (j+1) | (1 << i) | (1 << j)] = dp[k << (j+1)] + 2
                else:
                    # 两端不能形成回文，则取内部最大的
                    # 为什么可以把没取的位置也设为 1，因为最后都会遍历一遍找最佳，其实所有情况都考虑到了
                    for k in range(1 << (i - j - 1)):
                        dp[k << (j+1) | (1 << i) | (1 << j)] = max(dp[k << (j+1) | (1 << i)], dp[k << (j+1) | (1 << j)])
                
        result = 0
        for i in range(1 << n):
            result = max(result, dp[i] * dp[i ^ ((1 << n) - 1)])
        return result
# @lc code=end
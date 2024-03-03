#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    
    '''
        从每个字符中间向两边找
        不使用额外空间
        时间复杂度 O(n^2)
    '''
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        length = len(s)
        # 奇偶两种情况
        def spanOut(i): # 从一个字符开始往两侧找
            left = i-1
            right = i+1
            span1 = 0
            while left >= 0 and right < length and s[left] == s[right]:
                    span1 += 1
                    left -= 1
                    right += 1
            
            left = i
            right = i + 1
            span2 = 0
            while left >= 0 and right < length and s[left] == s[right]:
                    span2 += 1
                    left -= 1
                    right += 1
            
            if 2 * span1 + 1 > 2 * span2:
                return s[i - span1 : i+span1 + 1]
            else:
                return s[i - span2 + 1 : i + 1 + span2]
        
        max_len = 0
        for i in range(length):
            t_s = spanOut(i)
            if len(t_s) > max_len:
                max_s = t_s
                max_len = len(t_s)
        
        return max_s
    
    '''
        动态规划
        先根据每个位置两侧构建状态矩阵
        然后在矩阵里查找
        时间空间都是 O(n^2)
    '''
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     if n < 2:
    #         return s
        
    #     max_len = 1
    #     begin = 0
    #     # dp[i][j] 表示 s[i..j] 是否是回文串
    #     dp = [[False] * n for _ in range(n)]
    #     for i in range(n):
    #         dp[i][i] = True
        
    #     # 递推开始
    #     # 先枚举子串长度
    #     for L in range(2, n + 1):
    #         # 枚举左边界，左边界的上限设置可以宽松一些
    #         for i in range(n):
    #             # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
    #             j = L + i - 1
    #             # 如果右边界越界，就可以退出当前循环
    #             if j >= n:
    #                 break
                    
    #             if s[i] != s[j]:
    #                 dp[i][j] = False 
    #             else:
    #                 if j - i < 3:
    #                     dp[i][j] = True
    #                 else:
    #                     dp[i][j] = dp[i + 1][j - 1]
                
    #             # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
    #             if dp[i][j] and j - i + 1 > max_len:
    #                 max_len = j - i + 1
    #                 begin = i
    #     return s[begin:begin + max_len]
# @lc code=end


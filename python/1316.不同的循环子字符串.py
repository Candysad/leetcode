#
# @lc app=leetcode.cn id=1316 lang=python3
#
# [1316] 不同的循环子字符串
#

# @lc code=start
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        '''
        滚动哈希
        将字符串中的字符按顺序求值组成哈希
        相邻两个字符变化可以在O(1) 时间内更新出一个新的字符串
        '''
        
        
        
        '''
        暴力
        '''
        # result = set()
        # n = len(text)
        
        # for i in range(n):
        #     for j in range(i+1, (n+i) // 2 + 1):
        #         if text[i:j] == text[j : j + j - i]:
        #             result.add(text[i : j + j - i])
        # return len(result)
# @lc code=end


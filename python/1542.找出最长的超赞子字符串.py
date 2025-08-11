#
# @lc app=leetcode.cn id=1542 lang=python3
#
# [1542] 找出最长的超赞子字符串
#
from collections import Counter
# @lc code=start
class Solution:
    def longestAwesome(self, s: str) -> int:
        '''
        字符串 → 按位存信息 → 哈希
        '''
        n = len(s)
        pre = {0: -1}
        
        nowhash = 0
        result = 1
        for i in range(n):
            num = int(s[i])
            nowhash  ^= (1 << num)
             
            for j in range(10):
                prehash = nowhash ^ (1 << j)
                if prehash in pre:
                    result = max(result, i-pre[prehash])
                
            if nowhash in pre:
                result = max(result, i-pre[nowhash])
            else:
                pre[nowhash] = i
        
        return result
# @lc code=end


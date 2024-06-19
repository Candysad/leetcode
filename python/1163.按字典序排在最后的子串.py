#
# @lc app=leetcode.cn id=1163 lang=python3
#
# [1163] 按字典序排在最后的子串
#
from functools import reduce
# @lc code=start
class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        _maxc = max(s)
        
        t = []
        lasti = s.index(_maxc)
        for i in range(lasti + 1, n):
            if s[i] != _maxc and lasti != -1:
                t.append(lasti)
                lasti = -1
            elif s[i] == _maxc:
                if lasti == -1:
                    lasti = i
        if lasti != -1:
            t.append(lasti)
        
        result = ""
        for i in t:
            result = max(s[i:], result)
        return result
# @lc code=end
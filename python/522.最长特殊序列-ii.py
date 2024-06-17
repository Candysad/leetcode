#
# @lc app=leetcode.cn id=522 lang=python3
#
# [522] 最长特殊序列 II
#
from collections import defaultdict
# @lc code=start
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def check(s, p):
            sl, pl = len(s), len(p)
            if sl > pl:return False
            ps = 0
            for i in range(pl):
                if ps == sl: break
                if p[i] == s[ps]:
                    ps += 1
            return ps == sl
        
        n = len(strs)
        result = 0
        for i in range(n):
            sign = True
            for j in range(n):
                if i == j: continue
                sign &= not check(strs[i], strs[j])
            
            if sign:
                result = max(result, len(strs[i]))
        
        return result if result else -1
# @lc code=end
#
# @lc app=leetcode.cn id=161 lang=python3
#
# [161] 相隔为 1 的编辑距离
#

# @lc code=start
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if abs(m - n) >= 2: return False
        
        if m == n:
            result = 0
            for i in range(m):
                if s[i] != t[i]: 
                    result += 1
                    if result == 2: return False
            
            return result == 1

        if m < n:
            s, t = t, s
            m, n = n, m
        
        if n == 0:
            return m == 1
        
        result = 0
        j = 0
        for i in range(m):
            if j == n: return i == m-1
            if s[i] != t[j]:
                result += 1
                if result == 2:
                    return False
            else:
                j += 1
        return True
# @lc code=end
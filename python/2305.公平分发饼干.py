#
# @lc app=leetcode.cn id=2305 lang=python3
#
# [2305] 公平分发饼干
#

# @lc code=start
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        m = len(cookies)
        stats = 1 << m
        table = [0] * stats
        
        for i, c in enumerate(cookies):
            now = 1 << i
            for j in range(now):
                table[now | j] = table[j] + c
        
        t = table.copy()
        for _ in range(1, k):
            for j in range(stats - 1, 0, -1):
                s = j
                while s:
                    c = t[j ^ s]
                    if table[s] > c: c = table[s]
                    if c < t[j]: t[j] = c
                    s = (s-1) & j
        return t[-1]    
# @lc code=end
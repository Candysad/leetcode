#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m = len(g)
        n = len(s)
        if n == 0:
            return 0
        g.sort()
        s.sort()
        
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if s[p2] >= g[p1]:
                p1 += 1
            p2 += 1
        return p1
        
# @lc code=end


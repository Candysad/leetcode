#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(list(s)) + '#'
        def manacher(s):
            n = len(s)
            d = [1] * n
            left, right = 0, -1
            for i in range(n):
                r = 1 if i > right else min(d[left + right - i], right - i + 1)
                while 0 <=  i - r and i + r < n and s[i-r] == s[i+r]:
                    r += 1
                d[i] = r
                if i + r - 1 > right:
                    left = i - r + 1
                    right = i + r - 1
            return d
        
        d = manacher(s)
        rv = 0
        ri = 0
        for i, v in enumerate(d):
            if v > rv:
                ri = i
                rv = v
        result = s[ri-rv+1 : ri+rv]
        return ''.join([c for i,c in enumerate(result) if i%2])
# @lc code=end


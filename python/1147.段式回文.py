#
# @lc app=leetcode.cn id=1147 lang=python3
#
# [1147] 段式回文
#

# @lc code=start
class Solution:
    def longestDecomposition(self, text: str) -> int:
        result = 0
        s = text
        while s:
            print(s)
            n = len(s)
            right = 1
            while right <= n // 2 and s[:right] != s[-right:]:
                right += 1
            
            if right == n // 2 + 1:
                return result * 2 + 1

            else:
                result += 1
                s = s[right:-right]
        return result * 2
# @lc code=end
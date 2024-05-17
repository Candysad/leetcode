#
# @lc app=leetcode.cn id=2810 lang=python3
#
# [2810] 故障键盘
#

# @lc code=start
class Solution:
    def finalString(self, s: str) -> str:
        result = ""
        for c in s:
            if c != "i":
                result += c
            else:
                result = result[::-1]
        
        return result
# @lc code=end


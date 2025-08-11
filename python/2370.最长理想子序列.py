#
# @lc app=leetcode.cn id=2370 lang=python3
#
# [2370] 最长理想子序列
#

# @lc code=start
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        table = [0] * 26
        
        for c in s:
            num = ord(c) - ord('a')
            table[num] = max(table[max(0, num-k) : min(26, num+k+1)]) + 1
        return max(table)
# @lc code=end


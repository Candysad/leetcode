#
# @lc app=leetcode.cn id=2606 lang=python3
#
# [2606] 找到最大开销的子字符串
#

# @lc code=start
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        price = [i for i in range(1,27)]
        for i, c in enumerate(chars):
            price[ord(c) - ord('a')] = vals[i]
        
        s = [ord(c) - ord('a') for c in s]
        
        result = price[s[0]]
        pre = price[s[0]]
        for i in s[1:]:
            if pre >= 0:
                pre += price[i]
            else:
                pre = price[i]
            result = max(result, pre)
        return result if result > 0 else 0
# @lc code=end
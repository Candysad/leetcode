#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        print(citations)
        for i, c in enumerate(citations):
            if c < i + 1:
                return i
        return i + 1
# @lc code=end
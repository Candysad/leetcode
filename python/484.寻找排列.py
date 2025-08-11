#
# @lc app=leetcode.cn id=484 lang=python3
#
# [484] 寻找排列
#

# @lc code=start
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        result = [1]
        rev = []
        now = 2
        for c in s:
            if c == 'D':
                if not rev:
                    rev.append(result.pop())
                rev.append(now)
                now += 1
            else:
                while rev:
                    result.append(rev.pop())
                result.append(now)
                now += 1
        while rev:
            result.append(rev.pop())

        return result
# @lc code=end


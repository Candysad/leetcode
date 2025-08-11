#
# @lc app=leetcode.cn id=277 lang=python3
#
# [277] 搜寻名人
#

# @lc code=start
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
class Solution:
    def findCelebrity(self, n: int) -> int:
        result = 0
        for i in range(1, n):
            if knows(result, i):
                result = i
        
        for i in range(n):
            if i == result: continue
            
            if knows(result, i):
                return -1

            if not knows(i, result):
                return -1

        return result
# @lc code=end
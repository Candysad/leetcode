#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)
        
        def check(k):
            i = n-1
            result = 0
            while i >= 0 and k < piles[i]:
                result += piles[i] // k + (1 if piles[i] % k else 0)
                i -= 1
            if i >= 0:
                result += i + 1
            return result
        
        left, right = 1, piles[-1]
        
        while left <= right:
            mid = (left + right) // 2
            c = check(mid)
            if c > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
# @lc code=end

